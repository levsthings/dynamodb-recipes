'use strict'
const AWS = require('aws-sdk')
const config = require('../config/config')

const dynamoDB = new AWS.DynamoDB({
    region: 'us-east-2',
    accessKeyId: config.id,
    secretAccessKey: config.key
})

const tableConfig = {
    TableName: 'ExampleTable'
}

dynamoDB.deleteTable(tableConfig, (error, data) => {
    error
        ? console.error('Unable to create table. Error:', JSON.stringify(error, null, 4))
        : console.log('Deleted table. Table description:', JSON.stringify(data, null, 4))
})
