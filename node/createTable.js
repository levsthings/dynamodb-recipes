'use strict'
const AWS = require('aws-sdk')
const config = require('../config/config')

const dynamoDB = new AWS.DynamoDB({
    region: 'us-east-2',
    accessKeyId: config.id,
    secretAccessKey: config.key
})

const tableConfig = {
    TableName: 'Example Table',
    KeySchema: [
        {AttributeName: 'id', KeyType: 'HASH'},
        {AttributeName: 'fact', KeyType: 'RANGE'}
    ],
    AttributeDefinitions: [
        {AttributeName: 'id', AttributeType: 'N'},
        {AttributeName: 'fact', AttributeType: 'S'}
    ],
    ProvisionedThroughput: {
        ReadCapacityUnits: 1,
        WriteCapacityUnits: 3
    }
}

dynamoDB.createTable(tableConfig, (error, data) => {
    error
        ? console.error('Unable to create table. Error JSON:', JSON.stringify(error, null, 4))
        : console.log('Created table. Table description JSON:', JSON.stringify(data, null, 4))
})
