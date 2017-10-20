/**
 * Scan the count of table.
 */
'use strict'
const AWS = require('aws-sdk')
const {config} = require('../config/config')

AWS.config.update({
    region: 'us-east-2',
    accessKeyId: config.id,
    secretAccessKey: config.key
})

const docClient = new AWS.DynamoDB.DocumentClient()

const params = {
    TableName: 'ExampleTable',
    ProjectionExpression: 'id'
}

docClient.scan(params, (error, data) => {
    error
        ? console.error('Unable to get item. Error:', JSON.stringify(error, null, 4))
        : console.log('Value: ', JSON.stringify(data, null, 4))
})
