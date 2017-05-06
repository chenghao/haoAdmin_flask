/**
 * Created by chenghao on 16-12-2.
 */
// 后台连接前缀，（包括api接口和static）
var remoteUrl = "";

var success_layer_option = {icon: 1, time: 2000};
var error_layer_option = {icon: 5, time: 2000};

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

function buildPage(laypage, page_no, total_page, callback){
    laypage({
        cont: 'page',
        pages: total_page, //总页数
        groups: 5, //连续显示分页数
        curr: page_no, //当前页数
        jump: function(obj, first) {
            if(!first) {
                if(callback){
                    callback(obj.curr);
                }
            }
        }
    });
}

function openwin(title, url, width, height) {
    var _width = !width ? "800px" : width + "px";
    var _height = !height ? "550px" : height + "px";

    layer.open({
        type: 2,
        title: title,
        shadeClose: false,
        shade: 0.8,
        maxmin: false, //开启最大化最小化按钮
        area: [_width, _height],
        content: getPrefixPath(url)
    });
}