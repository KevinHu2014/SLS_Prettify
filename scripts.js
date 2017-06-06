var i = 0;
var arr = ["https://sls.weco.net/node/28521","https://sls.weco.net/node/28534","https://sls.weco.net/node/28535","https://sls.weco.net/node/28536","https://sls.weco.net/node/28537","https://sls.weco.net/node/28538","https://sls.weco.net/node/28540","https://sls.weco.net/node/28543","https://sls.weco.net/node/28552","https://sls.weco.net/node/28539","https://sls.weco.net/node/28608","https://sls.weco.net/node/28609","https://sls.weco.net/node/28614","https://sls.weco.net/node/28615","https://sls.weco.net/node/28616","https://sls.weco.net/node/28667","https://sls.weco.net/node/28668","https://sls.weco.net/node/28690","https://sls.weco.net/node/28707"];
while(i<arr.length){
    var Frame = document.createElement("Iframe");
    Frame.src = arr[i];
    Frame.width = "90%";
    Frame.height = "500px";
    document.body.appendChild(Frame);
    i=i+1;
    }
