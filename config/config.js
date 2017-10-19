'use strict'
const fs = require('fs')
let localConfig

try {
    localConfig = JSON.parse((fs.readFileSync('./config/config.json', 'utf-8')))
    console.log('Parsed local configuration for AWS credentials.')
} catch (err) {
    console.error('Unable to parse local configuration for AWS credentials : ', err)
}

exports.config = {
    id: localConfig.ID,
    key: localConfig.KEY
}
