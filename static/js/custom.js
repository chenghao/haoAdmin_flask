/**
 * Created by chenghao on 16-12-2.
 */
// 后台连接前缀，（包括api接口和static）
var remoteUrl = "";

success_layer_option = {icon: 1, time: 2000};
error_layer_option = {icon: 5, time: 2000};

function getPrefixPath(url) {
    return remoteUrl + url;
}

function customHref(url) {
    location.href = getPrefixPath(url);
}

function ajaxReq(url, callback, param, method, async, error){
	$.ajax({
        url: getPrefixPath(url) + "?t=" + (new Date()).valueOf(),
        data: !param ? {} : param,
        type: !method ? "get" : method,
        dataType: "json",
		async: !async ? true : async,
        success: function (data) {
            if (callback) {
                callback(data);
            }
        },
        error: function(){
            if(error){
                error();
            }else{
                layer.msg("系统异常", error_layer_option)
            }
        }
    })
}

function _confirm(msg, callback1, callback2){
    layer.confirm(msg, {
        btn: ['确定', '取消'] //按钮
    }, function (index) {
        layer.close(index);

        if (callback1){
            callback1();
        }
    }, function () {
        if (callback2){
            callback2();
        }
    });
}