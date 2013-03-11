/**
 * Created with PyCharm.
 * User: ivaylo
 * Date: 3/10/13
 * Time: 8:48 PM
 * To change this template use File | Settings | File Templates.
 */

var myVar=setInterval(function(){myTimer()},1000);

function myTimer()
{
    var d=new Date();
    var t=d.toLocaleTimeString();
    document.getElementById("demo").innerHTML=t;

    /*add the request and the result from show_log*/
    new $.ajax({
        type: "GET",
        url: "/dungeonMaster/log/",
        async: true,
        // The function below will be reached when the request has completed
        success: function(transport)
        {
            document.getElementById("test").innerHTML=transport;
        }
    });
}