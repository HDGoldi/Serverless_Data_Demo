var https = require('https');
var util = require('util');

exports.handler = function(event, context) {
    console.log(JSON.stringify(event, null, 2));
    console.log('From SNS:', event.Records[0].Sns.Message);

    var postData = {
        "channel": "#aws-sns",
        "username": "AWS SNS via Lamda :: DevQa Cloud",
        "text": "*" + event.Records[0].Sns.Subject + "*",
        "icon_emoji": ":aws:"
    };

    var message = event.Records[0].Sns.Message;
    var severity = "good";

    postData.attachments = [
        {
            "color": severity, 
            "text": message
        }
    ];

    var options = {
        method: 'POST',
        hostname: 'hooks.slack.com',
        port: 443,
        path: '/services/TBHBLU5NJ/BHUUKSTMZ/7LydlKp2QhaibLriRPYVRtJF'
    };

    var req = https.request(options, function(res) {
      res.setEncoding('utf8');
      res.on('data', function (chunk) {
        context.done(null);
      });
    });
    
    req.on('good', function(e) {
      console.log('problem with request: ' + e.message);
    });    

    req.write(util.format("%j", postData));
    req.end();
};