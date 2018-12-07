require('dotenv').config();
const https = require('https');
const requestedCount = +(process.argv[2] || '6');
const formality = +(process.argv[3] || '1');

const parseList = (data) => {
    const people = data.split('\n').map(row => {
        const [name, count, formality] = row.trim().split('\t');
        return {
            name,
            count: +count,
            formality: +formality
        };
    });
    console.log(makePick(people, requestedCount, []));
};

const makePick = (people, countRequested, booked) => {
    if (!countRequested) {
        return booked.map(name => people.find(p => p.name === name));
    }

    const options = people.filter(p => (!booked || !booked.includes(p.name)) && p.count <= countRequested && p.formality <= formality);
    const pick = options[~~(Math.random() * options.length)];
    booked.push(pick.name);
    return makePick(people, countRequested - pick.count, booked);
};

https.get(process.env.LIST_URL, (res) => {
    let data = '';

    res.on('data', chunk => data += chunk);

    res.on('end', () => parseList(data));
});

