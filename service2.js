// service2.js
const express = require('express');
const os = require('os');

const app = express();
const PORT = 8200;

// Helper function to get IP addresses
const getIpAddresses = () => {
    const interfaces = os.networkInterfaces();
    const addresses = [];
    for (const key in interfaces) {
        for (const address of interfaces[key]) {
            if (address.family === 'IPv4' && !address.internal) {
                addresses.push(address.address);
            }
        }
    }
    return addresses;
};

app.get('/service2', (req, res) => {
    const hostname = os.hostname();
    const ipAddresses = getIpAddresses();
    res.json({
        hostname: hostname,
        ipAddresses: ipAddresses,
    });
});

app.listen(PORT, () => {
    console.log(`Service2 running on port ${PORT}`);
});
