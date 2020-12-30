# Discord-LOL-bot
## 리그 오브 레전드 소환사 검색 디스코드 봇
## League of Legends Summoner Searching Discord Bot
---
beautifulsoup4를 활용하여 OP.GG에서 소환사 정보를 크롤링해서 디스코드 메시지로 보여주는 봇  
A bot that uses beautifulsoup4 to crawl summoner information from OP.GG and display it as a Discord message.

### 사용 방법
1. Git clone
```
$ git clone https://github.com/Ohzzi/Discord-LOL-Bot.git
$ cd Discord-LOL-Bot
```
2. Discord 어플리케이션 생성
```
- https://discord.com/developers/applications 로 접속해서 새 어플리케이션을 만든다.
- Client ID 를 저장하고, Bot 항목으로 가서 Create a Bot User 클릭
- token을 프로젝트 경로에 token.json이라는 파일로 저장한다.
```
- token.json
```
{
    "token": "Input_Your_Token"
}
```
3. 서버에 봇을 추가
```
- https://discord.com/oauth2/authorize?client_id=CLIENT_ID&scope=bot에 접속한다.
- 이 때, CLIENT_ID에 생성한 어플리케이션의 Client ID를 입력한다.
- 봇을 추가할 디스코드 서버에 봇을 추가한다.
```
4. 봇 실행
```
$ python Bot.py
```