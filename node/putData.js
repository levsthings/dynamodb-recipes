/**
 * Loading the table with ./exampledata/data.json
 */
'use strict'
const fs = require('fs')
const AWS = require('aws-sdk')
const {config} = require('../config/config.js')

AWS.config.update({
    region: 'us-east-2',
    accessKeyId: config.id,
    secretAccessKey: config.key
})

const docClient = new AWS.DynamoDB.DocumentClient()

let parsedData

try {
    parsedData = JSON.parse(fs.readFileSync('./exampleData/data.json', 'utf-8'))
} catch (err) {
    console.error('Unable to parse data: ', err)
}

parsedData.data.map((item) => {
    const params = {
        'TableName': 'ExampleTable',
        'Item': {
            'id': item.id,
            'fact': item.fact
        }
    }
    docClient.put(params, (error, data) => {
        error
            ? console.error('Unable to add. Error: ', JSON.stringify(error, null, 4))
            : console.log('PutItem succeeded: ', JSON.stringify(item, null, 4))
    })
})
