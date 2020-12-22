const Discord = require("discord.js");
const Sequelize = require('sequelize');
const open = require('open');
require('dotenv').config();

const client = new Discord.Client()
const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: 'database.sqlite'
});
const history = sequelize.define('history', {
	id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        primaryKey: true
    },
    by:{
        type: Sequelize.STRING,
        allowNull: false
    },
	link: {
        type: Sequelize.STRING,
        allowNull: false
    },
    done:{
        type: Sequelize.BOOLEAN,
        allowNull: false,
        defaultValue: false
    }
});
client.login(process.env.API_KEY);

client.on("ready", () => {
    console.log(`Logged in as ${client.user.tag}!`);
    if(check()) history.sync();
});

client.on("message", async msg => {
    if (msg.author.bot) return;
    if(msg.channel.id === "790774106684915713"){
        cnt = msg.content;
        if(cnt.includes('meet.google.com')){
            cnt.split(' ').forEach(e => {
                if(e.includes("meet.google.com")){
                    url = "https://meet.google.com/"+e.split('/')[e.split('/').length-1];
                    openLink(url,msg);
                }
            });
        }
    }
});
async function openLink(url,msg){
    const ele = await history.findOne({ where: { link: url} });
    history.create({
        by : msg.author.id,
        link : url,
        done : true
    });
    if(!ele) open(url);
}
async function check(){
    try {
        await sequelize.authenticate();
        console.log('Connection has been established successfully.');
        return true ;
    } catch (error) {
        console.error('Unable to connect to the database:', error);
    }
    return false ;
}