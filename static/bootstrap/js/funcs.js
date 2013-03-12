/**
 * Created with PyCharm.
 * User: ivaylo
 * Date: 3/11/13
 * Time: 7:58 PM
 * To change this template use File | Settings | File Templates.
 */

function roll()
{
    new $.ajax({
        type: "GET",
        url: "/dungeonMaster/roll/",
        async: true,
        success: function(response){
            myTimer()
        }
    });


}

function action(id)
{
    $.post("/dungeonMaster/action/", {actid: id}, function(response){
        myTimer()
    })
}

function myTimer()
{
    /*add the request and the result from show_log*/
    new $.ajax({
        type: "GET",
        url: "/dungeonMaster/log/",
        async: true,
        // The function below will be reached when the request has completed
        success: function(transport)
        {
            document.getElementById("test").innerHTML=transport;
            scrollable()
        }
    });
}

function scrollable()
{
    var objDiv = document.getElementById("console");
    objDiv.scrollTop = objDiv.scrollHeight;
}