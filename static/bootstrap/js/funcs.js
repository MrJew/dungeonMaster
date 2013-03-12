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
            refreshConsole()
        }
    });


}

function refreshStats(){
    $.post("/dungeonMaster/refreshstats/", function(response){
        var n = response.split(",");
        refreshDiv(n[0],n[1],n[2],n[3],n[4],n[5],n[6])
    })
}

function action(id)
{
    $.post("/dungeonMaster/action/", {actid: id}, function(response){
        refreshConsole()
    })
}

function refreshConsole()
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

function refreshDiv(charName, charLvl, charHp, charMana, charXP, charAP, charSP){
    var maxHp=100
    var maxMana=100
    var maxAp=100
    $("#stats").hide().html("<table class='table table-striped' > <tr><td><b>"+charName+"</b></td><td>"+charLvl+"</td></tr>" +
        "<tr class='error'><td><b>Hit Points:</b></td><td>"+charHp+"/"+maxHp+"</td></tr><tr class='info'><td><b>Mana:</b></td><td>"+charMana+"/"+maxMana+"</td></tr>" +
        "<tr class='warning'><td><b>XP:</b></td><td>"+charXP+"</td></tr><tr class='success'><td><b>Action Poitns:</b></td><td>"+charAP+"/"+maxAp+"</td></tr>" +
        "<tr class='sp'><th><b>Skill Points</b></th><td>"+charSP+"</td></tr></table>").fadeIn('fast');
}
