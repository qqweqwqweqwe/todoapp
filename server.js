// http://localhost:8080/  항상 여기로 접속하세용

const express = require("express"); // 아까 설치한 라이브러리를 첨부해주세요
const app = express(); // 이해할 필요는 없다 그냥 express 라이브러리 사용법임   // import 로 하면 안됨
const bodyparser = require("body-parser");
const methodOverride=require('method-override')
const crypto=require("crypto")
const http=require('http').createServer(app)
const {Server}=require('socket.io')
const io = new Server(http) 
let multer=require('multer')
var cookieParser = require('cookie-parser');


var storage=multer.diskStorage({
  destination:function(req,file,cb){
    cb(null, './public/image')   // 이미지를 어디로 보낼지, 폴더 경로 업로드한 이미지가 저장될 위치
  },
  filename: function(req, file, cb){
    cb(null, file.originalname) // 파일명을 설정하는것 여기선 오리지날 네임을 갖다 쓰는거임 
  },
  filefilter :function(req,file,cb){
    //이거는 파일 필터 ex 이미지만 업로드
  }
})

app.use(bodyparser.urlencoded({ extended: true }));
app.use(methodOverride('_method'))
app.set('view engine', 'ejs')
app.use(cookieParser());


function createhashpassword(password){   // 문자열 형태로 넣어줘야함
  return crypto.createHash("sha512").update(password).digest('base64')
}

app.use('/public', express.static('public'))
const MongoClient = require("mongodb").MongoClient;

var db;
MongoClient.connect(
  "mongodb+srv://k0789789:1035317a!@cluster0.6ojrbcz.mongodb.net/?retryWrites=true&w=majority",
  function (에러, client) {
    // 몽고 db로 연결
    if (에러) {
      return console.log(에러);
    }
    db=client.db('todoapp')
    // 서버는 암기가 중요하다 이해하려 하지말자 서버코드 이해하려고 하지마셈

    http.listen(8080, function () {
      /// 8080 서버띄울 포트 번호 function 띄운 후 실행할 코드  6만개의 포트중 8080으로 들어온

      console.log("listening on 8080"); //애들은 함수 실행
    }); // 서버를 여는 행위임
  }
);

// 데이터베이스는 일종의 폴더
// 데이터 베이스는 일종의 파일ㅇ

app.get("/pet", function (요청, 응답) {
  응답.send("펫쇼핑 사이트 입니다");
  // html send하면 펫용품 사이트랑 다를게 없당 ㅎㅎ
});

//누군가가 /pet 으로 방문을 하면
//pet 관련된 안내문 띄워주자

app.get("/beauty", function (요청, 응답) {
  응답.send("뷰티용품 사이트 입니다");
  // html send하면 펫용품 사이트랑 다를게 없당 ㅎㅎ
});

app.get("/", (요청, 응답) => {
  // function 을 => 로 바꿔서 쓰는거 후자가 신문법임
  응답.render('index.ejs',{})
  // html send하면 펫용품 사이트랑 다를게 없당 ㅎㅎ
});




//어떤 사람이 /add 경로로 post 요청을 함녀
// ??를 해주세요


// /list 로 get 요청하면 html 을 보여줌
// 실제 db에 저장된 데이터들로 꾸며진 html

app.get("/list", function (요청, 응답) {
  db.collection('post').find().toArray(function(에러,결과){
    응답.render("list.ejs",{ posts : 결과, 아이디 : 요청.user});

  });     //어떤 파일명이 post 라는것을 다루겠습니다

  //디비에 저장된 post collection 안의 제목이 뭐인 라는 이름을 가진 데이터를 꺼내주세요

});


// detail/글번호로 접속하면 detail.ejs 보여줌

//1 없는 게시물 처리
//2 글 제목 누르면 상세페이지로 이동하기 

app.get('/detail/:id', function(요청, 응답){  // :id 이 의미는 슬래쉬디에 아무 문자열이나 입력하면 밑에있는거 실행해달라는 뜻 
  요청.params.id=parseInt(요청.params.id)
  db.collection('post').findOne({_id : 요청.params.id /*url 의 파라미터중 :id에 해당하는 것  */}, function(에러, 결과){
    if(결과==null){
      응답.end('not found')     // 에러가 발생하였을 때 웹페이지 상에 not found 걸어줌
    }
    else{
    console.log(결과)
    응답.render('detail.ejs', {data : 결과 })  // ejs 파일로 데이터를 전송하는 법
    }
  })
})

app.get('/edit/:id', function(요청, 응답){
  db.collection('post').findOne({_id : parseInt(요청.params.id)},function(에러,결과){
    console.log(결과)
    응답.render('edit.ejs',{post : 결과} )
  })
})

app.get('/edit', function(요청,응답){
  var postid=요청.body.edit
  console.log(요청.body)
  응답.redirect('/edit:'+postid)
  console.log('ㅎㅎ병신')
})


// 서버로 put 요청 들어오면 게시물 수정 처리하기
app.put('/edit', function(요청, 응답){
  // 폼에서 전송한 데이터의 id를 통해 제목 날짜 업데이트
  db.collection('post').updateOne({_id : parseInt(요청.body.id)},{$set:{ 제목: 요청.body.title, 날짜:요청.body.date}}, function(에러,결괴){
    console.log('수정완료')
    // 변경을 하고나면 다른페이지로 이동해야지
    응답.redirect('/list') // 서버에서는 응답이 꼭! 필요함 응답을 해주지 않으면 사이트가 멈춰버림 
  })
})

///// 여기까지 crud 다배움


const passport=require('passport')   // 지금에서야 나온건데 이것의 의미는 나는 server.js 에서 passport라는 라이브러리 쓸거에요 라는 뜻
const LocalStrategy=require('passport-local').Strategy
const session=require('express-session');
const { render } = require("ejs");
const { send } = require("process");

app.use(session({
  secret : '비밀코드',
  resave: true,
  saveUninitialized : false
}))
app.use(passport.initialize())
app.use(passport.session())

app.get("/write", 로그인했니, function (요청, 응답) {
  
  응답.render('write.ejs',{})
});


function 로그인안했니(요청,응답,next){
  if(요청.user){
    응답.render('already_login.ejs')
  }
  else{
    next()
  }
}

// app.use 나는 미들웨어를 쓰겠습니다 라는 뜻
app.get('/login', 로그인안했니,function(요청, 응답){     // 어떤 사람이 
  응답.render('login.ejs')
  // 아이디 비번 맞으면 로그인 성공 페이지로 보내줘야함 
})

app.post('/login', passport.authenticate('local', {
  failureRedirect:'/fail'
}), function(요청, 응답){    //passport허용하면 뒤에있는 함수 실행 //어떤 사람이 로그인 폼을 전송하면...LocalStrategy.
  // 아이디 비번 맞으면 로그인 성공 페이지로 보내줘야함 
  응답.redirect('/')
  // 회원인증 실패하면 /fail로 성공하면 그 밑의 경로로
})

app.get('/mypage', 로그인했니,function(요청,응답){
  console.log(요청.user)
  응답.render('mypage.ejs',{사용자 : 요청.user}) //성공하면 mypage.ejs 로 뒤에있는건 mypage.ejs에 보내는 데이터 //요청.user를 '사용자'라는 데이터 명으로 보냄
})

function 로그인했니(요청,응답,next){
  if(요청.user){  //로그인후 세션이 있으면 항상 요청.user 가 있음  //요청.user 에는 몽고db안의 id 와 pw등이 들어가 있음
    next()   // 로그인 한 상황이면 그 다음으로 보내줌
    
  }
  else{
    응답.redirect('/login')
  }
}


passport.use(new LocalStrategy({
  usernameField: 'id',   // 폼에 id
  passwordField: 'pw',   // 폼에 pw
  session: true,
  passReqToCallback: false,
}, function (입력한아이디, 입력한비번, done) {  // 여기서 부터가 사용자의 아이디와 비번을 검증하는 내용 
  console.log(입력한아이디, 입력한비번);
  db.collection('login').findOne({ id: 입력한아이디 }, function (에러, 결과) {
    if (에러) return done(에러)
    if (!결과) return done(null, false, { message: '존재하지않는 아이디요' }) // 결과에 아무것도 없을 때 
    if (입력한비번 == 결과.pw) {
      return done(null, 결과)
    } else {
      return done(null, false, { message: '비번틀렸어요' })
    }
  })
}));

// id를 이용해서 세션을 저장시키는 코드(로그인 성공시 발동)
passport.serializeUser(function(user,done){
  done(null, user.id)
})

// 이 세션 데이터를 가진 사람을 db에서 찾아주세요(마이페이지 접속시 발동)
passport.deserializeUser(function(아이디,done){    // 여기있는  '아이디'가 위에 serializeruser 에 user.id와 동일함
  db.collection('login').findOne({id:아이디},function(에러,결과){
    done(null, 결과)  //마이페이지 접속시 db에서 id 어쩌구 인걸 찾아서 그 결과를 보내줌
  })
})

// 삭제  // list.ejs
app.delete('/delete', 로그인했니,function(요청, 응답){
  console.log(요청.body)
  // 요청.body._id는 글번호
  요청.body._id=parseInt(요청.body._id)
  console.log(요청.user)
  db.collection('post').findOne(요청.body,function(에러,결과){
    if(결과.작성자==요청.user.id){
      db.collection('post').deleteOne(요청.body,function(에러, 결과){
        console.log('삭제완료')
        응답.status(200).send({messege : '성공했습니다'})
      })
    }
    else{
      응답.status(400).send({message:'실패요 ㅎㅎ'})  //이렇게 해주어야함 이전처럼 응답.send("이런식으로 하면 ㄴㄴ임 ㅎㅎ")
      
    }
  })
})


// 회원가입 만들기

app.get('/register',로그인안했니,function(요청,응답){
  응답.render('register.ejs')
})

app.post('/register', function(요청,응답){
  db.collection("login").findOne({id : 요청.body.id }, function(에러,결과){
    if(결과!=null){
      // 기존 회원 db에 중복 아이디가 있는거니까 에러창으로 옮겨주어야함
      응답.redirect('/fail')
    }
    else{
      db.collection('login').insertOne({ id: 요청.body.id, pw: 요청.body.pw}, function(에러,결과){
        응답.redirect('/')
        // ㅎㅎ  정상 작동 된다 ㅎㅎ ㅎㅎ ㅎㅎㅎ ㅎㅎㅎㅎ
        // 이제 할거는 그거임 회원가입 하면 비밀번호 암호화-복호화 거쳐서 데이터베이스에 저장하는 것
        // 아이디에 알파벳과 숫자만 있는지 체크하는것 
        // 로그인 할때는 역과정 거쳐서 로그인하게 해주는것 

      })
    }
  })
})

app.get('/fail', function(요청,응답){
  응답.render('fail.ejs')
})
app.get('/search', (요청,응답)=>{

  searchvalue=요청.query.value
  var searchCondition = [    // 검색 조건
    {
      $search: {
        index: "search", // 제작한 search index 이름
        text: {
          query: searchvalue,
          path: "제목", //제목과 날짜 둘다 찾고 싶으면 ['제목', '날짜']
        },
      },
    },
    { $sort: { _id: 1 } }, // _id를 기준으로 오름차순 정렬  // binary search 를 써야 하기 때문이당 ㅎㅎ 
    { $limit: 10 }, // 검색결과 10개로 제한
    // { $project: { 제목: 1, _id: 0 } }, // 보여줄 결과를 정하는 부분
  ];
  // db.collection('post').find({제목 :/글쓰기/}).toArray(function(에러,결과)  -> 글쓰기가 포함된 게시글들 전부 검색 근데 find로 찾으면 ㅈㄴ 느림
  db.collection('post').aggregate(searchCondition).toArray(function(에러,결과){  //aggregate 안에 검색 조건 넣어주면 검색 시작
  
    응답.render('search.ejs', {posts : 결과})
  })
  // 숙제 알아서 검색 기록 파일 만들어 오기 

})

app.post(
  "/add",
  function (요청, 응답) {
    
    // 여기 '요청' 안에 전달된 정보가 있다
    // 요청.user== 현재 로그인한 사람의 정보가 들어가있다
    db.collection("counter").findOne({name:'게시물갯수'}, function(에러,결과){
      console.log(결과.totalpost)
      var 총게시물갯수=결과.totalpost
      var 저장할거={
        _id:총게시물갯수+1,
        제목:요청.body.title,
        작성자:요청.user.id, 
        날짜:요청.body.date,
      }
      db.collection("post").insertOne(
        저장할거, function(에러, 결과){
          if(!에러){
            console.log('저장완료')
          }
        db.collection('counter').updateOne({name:'게시물갯수'},{$inc :{totalpost:1} },function(에러, 결과){
          // 콜백함수는 순차적으로 실행하고 싶을때 사용한다
          // 즉 a, b, func 이런식으로 있을때 a b 수행하고 func 실행해주세요 할때 쓰는거임
          if (에러){return console.log(에러)} // 에러에 자신있으면 callback 함수를 지워도 됨 
        })
        // 업데이트 연산자 $set은 바꿔주세요 즉 totalpost라는 값을 바꿔주세요 할때 쓰는 연산자
        // 연산다 $inc는 totalpost 의 값에 얼마만큼 더해주세요  당연히 음수도 가능
        

        });
      

    });
    응답.redirect('/write')
    // 서버는 암기가 중요하다 이해하려 하지말자 서버코드 이해하려고 하지마셈
  }

  // DB 에 저장해주세요 라는 명령이 필요함  rest api
  // api 는 rest 하게 만드는게 좋아요
  // api 는 서버와 고객간의 요청 방식이다. 웹 개발 상에서는
);

app.use('/shop', require('./routes/shop.js'))  // app.use(미들웨어) 미들웨어는 요청과 응답 사이에 실행되는 코드  '/shop'경로로 들어온 모든 사람들에게 적용되는 미들웨어 (라우터) 

app.use('/board',require('./routes/board.js') )

var upload=multer({storage: storage})

app.get('/upload', function(요청,응답){
  응답.render('upload.ejs')
}) // 업로드한 이미지는 보통 작업폴더 안에 저장함

app.post('/upload', upload.single("profile"), function(요청,응답){  //single 은 파일 하나, array는 여러개 
  응답.send('업로드완료')
})  //어떤 사람이 업로드 페이지에서 포스트 요청을 했을때 파일을 저장해주세요~ 라는 기능
// 이미지 업로드시 멀터를 미들웨어로 동작시키기 

app.get('/image/:imagename', function(요청,응답){
  
  응답.sendFile(__dirname+'/public/image/'+요청.params.imagename)
})

// 채팅기능 구현하기
// 채팅은 사실 댓글과 비슷하다 그러나 실시간성이 추가된 것일뿐..
// 댓글도 그냥 게시물 발행임
// 대부분의 db형식은 게시물 발행과 결이 비슷하다고 보면 된다 한 90퍼 정도?
// 어떤 부모게시물에 달린 댓글인지, 즉 종속관계 명확하게 명시해주어야함 
// 게시물간의 종속관계를 표현해주고 싶을때, 부모정보까지 저장해두면 된다.

app.get('/chat/:id', 로그인했니,function(요청,응답){
  // 여기서 가져오는 거야
  응답.render('chat_detail.ejs',{채팅방번호 : 요청.params.id})
})

app.get('/chat',로그인했니,function(요청,응답){
  // 현재 내가 속해있는 채팅방들 목록을 보여준다
  console.log(요청.user.id)

  db.collection('chatroom').find({member:요청.user.id}).toArray(function(에러,결과){

    접속한아이디=요청.user.id

    응답.render('chat.ejs',{접속한아이디: 요청.user.id, posts: 결과})  
  })
})

app.post('/chat/:id',로그인했니,function(요청,응답){
  게시글번호=요청.params.id
  db.collection('post').findOne({_id : parseInt(요청.params.id)}, function(에러,결과){
    글작성자=결과.작성자
    var 저장할거={
      member: [결과.작성자, 요청.user.id],
      date: new Date(),
      title : 요청.params.id
    }
    // 중복된 데이터가 있으면 채팅창 리스트에 추가로 넣으면 안되고, 이동을 시켜줄거야
      db.collection("chatroom").findOne({member : 저장할거.member},function(에러,결과){
        console.log(글작성자, 요청.user.id)
        if(글작성자==요청.user.id){
          응답.redirect('/chat')
        }
        else if(결과==null){
          db.collection("chatroom").insertOne(저장할거, function(에러,결과){
            console.log('채팅방 개설 완료!')
            응답.redirect('/chat')
          })
        }
        else{
          console.log("채팅방 이미있음")
          응답.redirect('/chat')
        }
      })
  })
})

app.post('/message',로그인했니,function(요청, 응답){
  var 저장할거={
    parent: 요청.body.parent,
    content:요청.body.content,
    sender : 요청.user.id,
    date: new Date()
  }
  db.collection('message').insertOne(저장할거,function(에러,결과){
  })
  // console.log(저장할거)    // 여기의 요청.body 는 ejs 파일에서 ajax 로 전덜해준 데이터를 의미한다
})

// 실시간으로 채팅 구현하는 방법은 크게 두가지가 있다
// 1. 계속 get 요청 날리는 방법 근데 이거 사용자 많아지면 매우 비효율적
// 2. 

app.get('/message/:id', 로그인했니, function(요청,응답){
  응답.writeHead(200,{
    "Connection" : "keep-alive",
    "Content-Type" : "text/event-stream",
    "Cache-Control" : "no-cache",
  })

  db.collection('message').find({ parent:요청.params.id}).toArray().then((결과)=>{  //then의 의미는 앞서 진행한 것들이 성공 하면~~? 이라는 의미
    응답.write('event: test\n'); //유저에게 데이터 전송은 event:보낼데이터 이름
    응답.write('data:'+ JSON.stringify(결과) +'\n\n'); // data:보낼데이터    // 서버에서 실시간 전송시 문자 자료만 가능 위에 .toarray로 인해 배열로 전달돼서 깨질거임
    // json 자료로 바꿔준다.
  })

  // 실시간으로 서버에 데이터 전송하는 법
  // 이제 /어쩌구로 get 요청하면 실시간 채널 오픈됩니다
  // 서버와 유저간 실시간 소통채널 열기
  // 일반적인 get post 방식은 한번 요청시 한번 응답 그러나
  // 위에 형식 처럼 하면 여러번 응답이 가능해진다

  // 헤더라는것이 무엇인가?
  // http 요청시 몰래 전달되는 정보들이 담겨있는 부분이 바로 헤더이다

  // 채팅방에서 엔터를 눌러도 바로바로 프론트로 보이지 않음
 // 오늘 그거 구현할거임 
 // db 가 업데이트 되면 유저에게 쏴주세요~~
 // 근데 db는 수동적이라 그런거 잘 못함--> 몽고디비 체인지 스트림 쓰면 가능해짐 이걸쓰면 디비 변동시 서버에 알려줌 유저에게 보낼 수 있음

  const pipeline = [
    { $match: { 'fullDocument.parent': 요청.params.id } } // 컬렉션 안에 원하는 document만 감시할지 정하는 것 //부모가 params.id 인것만 감시
  ];
  const collection=db.collection('message')
  const changeStream=collection.watch(pipeline)  // watch 함수가 감시하는 거임
  changeStream.on('change',(result)=>{
    응답.write('event: test\n')                     // 시발 이게 문제였네 이거 하나때문에 계속 갱신 안되고 새로고침 존나했네 씨발련 진짜 아;
    응답.write(`data: ${JSON.stringify([result.fullDocument])}\n\n`); // db에 변동이 생기면 응답해주세요 
  })
})




// 자기가 쓴글만 삭제할 수 있도록 바꾸장 ㅎㅎ
// 글이 삭제되더라도 채팅 내용은 안삭제되게 냅두는게 맞다 ㅇㅇ



//웹소켓이라는 것을 쓰면 서버 유저와 실시간 소통이 가능하다
// 웹소켓이라는 것은 유저가 보는 html 파일에도 소켓을 세팅해놓아야 한다
app.get('/socket',function(요청,응답){
  응답.render('socket.ejs')
})

io.on('connection', function(socket){   // 여기 socket에는 유저의 정보가 담겨있음
  // 어떤 사람이 웹소켓에 접속하면 실행해달라는 함수임
  console.log('유저 접속함')
  // socket.id 이게 접속한 유저의 uniq한 소켓 아이디
  socket.on('joinroom', function(data){
    socket.join('room1')
    // joinroom 이라는 메세지를 받으면 room1에 입장시켜줘~ 라는 뜻 
    // 이 유저는 이제 room1에서만 채팅을 할 수 있음 

  })
  socket.on('room1-send', function(data){
    io.emit('broadcast', data)  // 이건 모든 유저에게 브로드캐스트 해주는것 
    io.to('room1').emit('broadcast', data) // room1에 들어간 유저에게만 메세지 
    // 이것의 실행 결과는 다음과 같음
    // user1 과 user2가 각각 있다고 가정할때 user1은 채팅방1입장 버튼을 누르고 user2는 안눌렀을때 
    // user1이 채팅방1에서 메세지 보내기 누름녀 user2에게 메세지 안들어감
  })
// 서버가 수신하는 코드
socket.on('user-send',function(data){  // 유저가 보낸 메세지가 data   유저가 보낸 메세지 수신
  // 누가 user-send라는 이름으로 메세지 보내면 실행해주세요 라는 함수임
  io.emit('broadcast',data)   //유저에게 서버가 메세지 전송  io.emit은 모든 유저에게 메세지 보낸다 
  // io.to(socket.id).emit('broadcast',data)   //지금 접속한 유저에게만 메세지 보낼 수 있음

})
})

// 서버가 수신하는 코드

// 혼자할거는 1ㄷ1채팅 서비스 만들기 





// 로그 아웃
// 로그아웃 시켜줄 뿐 만 아니라, 사이트 내에 존재하는 쿠키 또한 삭제해줌

app.get('/logout', function (요청, 응답){
  요청.session.destroy(function (err) {
    응답.clearCookie('connect.sid');
    응답.redirect('/'); //Inside a callback… bulletproof!
  });
});

