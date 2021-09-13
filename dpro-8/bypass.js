const thrift = require('thrift-http');
const LineService = require('LineService');

var _client = '';
var gid = '';
var uids = [];
var invite = [];
var token = ''; 

process.argv.forEach(function (val) {
  if(val.includes('gid=')){
	  gid = val.split('gid=').pop();
  }else if(val.includes('uid=')){
	  uids.push(val.split('uid=').pop());
  }else if(val.includes('uik=')){
	  invite.push(val.split('uik=').pop());
  }else if(val.includes('token=')){
	  token = val.split('token=').pop();
  }
});

function setTHttpClient(options) {
    var connection =
      thrift.createHttpConnection('legy-jp.line.naver.jp', 443, options);
    connection.on('error', (err) => {
      console.log('err',err);
      return err;
    });
    _client = thrift.createHttpClient(LineService, connection);
  }
  
  
setTHttpClient(options={
    protocol: thrift.TCompactProtocol,
    transport: thrift.TBufferedTransport,
    headers: {'User-Agent':'Line/9.22.2','X-Line-Application':'IOS\t9.22.2\tIOS\t13.2.3','X-Line-Access':token},
    path: '/S4',
    https: true
    });
	
for (var i=0; i < uids.length; i++) {
  _client.cancelGroupInvitation(0, gid, [uids[i]]);
  _client.kickoutFromGroup(0, gid, [uids[i]]);
}

async function func1() {

  let promise1 = new Promise((resolve, reject) => {
    
    try {
    for (var i=0; i < invite.length; i++) {
      _client.inviteIntoGroup(0,gid,invite);
    }
    resolve("[ NOTIF ] ['Done']")
    } catch(e) {
    reject(e);
    }
  });
  return promise1;
}
var promise1 = func1();

Promise.all([promise1])
  .then(results => console.log(results));