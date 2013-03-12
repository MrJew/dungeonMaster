/**
 * Created with PyCharm.
 * User: ivaylo
 * Date: 3/11/13
 * Time: 7:58 PM
 * To change this template use File | Settings | File Templates.
 */

function roll()
{
    var num = document.getElementById('infoHolder').value
    if (num<=0){
        num=1
    }
    $.post("/dungeonMaster/roll/", {rolls: num}, function(response){
        refreshConsole()
    });
}

function refreshStats(id){
    $.post("/dungeonMaster/refreshstats/",{actid: id} , function(response){
        var n = response.split(",");
        refreshDiv(n[0],n[1],n[2],n[3],n[4],n[5],n[6], n[7], n[8], n[9])
    })
}

function action(id, type)
{
    $.post("/dungeonMaster/action/", {actid:id,typeid:type}, function(response){
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

function refreshDiv(charName, charLvl, charHp, charMana, charXP, charAP, charSP, maxHp, maxMana, maxAp){

    $("#stats").hide().html("<table class='table table-striped' > <tr><td><b>"+charName+"</b></td><td>"+charLvl+"</td></tr>" +
        "<tr class='error'><td><b>Hit Points:</b></td><td>"+charHp+"/"+maxHp+"</td></tr><tr class='info'><td><b>Mana:</b></td><td>"+charMana+"/"+maxMana+"</td></tr>" +
        "<tr class='warning'><td><b>XP:</b></td><td>"+charXP+"</td></tr><tr class='success'><td><b>Action Poitns:</b></td><td>"+charAP+"/"+maxAp+"</td></tr>" +
        "<tr class='sp'><th><b>Skill Points</b></th><td>"+charSP+"</td></tr></table>").fadeIn('fast');
}
