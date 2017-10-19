/**
 * Querying a single item based on key='id
 */
'use strict'
const AWS = require('aws-sdk')
const config = require('../config/config')

AWS.config.update({
    region: 'us-east-2',
    accessKeyId: config.id,
    secretAccessKey: config.key
})

const docClient = new AWS.DynamoDB.DocumentClient()

const params = {
    TableName: 'ExampleTable',
    KeyConditionExpression: 'id = :hkey',
    ExpressionAttributeValues: {
        ':hkey': 24
    }
}

docClient.query(params, (error, data) => {
    error
        ? console.error('Unable to get item. Error:', JSON.stringify(error, null, 4))
        : console.log('Value: ', JSON.stringify(data, null, 4))
})
