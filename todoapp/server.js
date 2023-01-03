const express = require("express"); // 아까 설치한 라이브러리를 첨부해주세요
const app = express(); // 이해할 필요는 없다 그냥 express 라이브러리 사용법임   // import 로 하면 안됨
const bodyparser = require("body-parser");
const methodOverride=require('method-override')
const crypto=require("crypto")

let multer=require('multer')

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

    app.listen(8080, function () {
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
    console.log(결과);
    응답.render("list.ejs",{ posts : 결과});

  });     //어떤 파일명이 post 라는것을 다루겠습니다

  //디비에 저장된 post collection 안의 제목이 뭐인 라는 이름을 가진 데이터를 꺼내주세요

});

app.delete('/delete', function(요청, 응답){
  console.log(요청.body)
  요청.body._id=parseInt(요청.body._id)
  db.collection('post').deleteOne(요청.body,function(에러, 결과){
    console.log('삭제완료')
    응답.status(200).send({messege : '성공했습니다'})
  })
})

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
    응답.send('이미 로그인 하셨어요')
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
    응답.send('로그인 안하셨는데요?')
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

// 회원가입 만들기

app.get('/register',function(요청,응답){
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

app.get('/chat/:id', function(요청,응답){
  // 여기서 가져오는 거야
  응답.render('chat.ejs',{채팅방번호 : 요청.params.id})
})

app.post('/chat/:id', function(요청,응답){
  게시글번호=요청.params.id
  db.collection('post').findOne({_id : parseInt(요청.params.id)}, function(에러,결과){
    var 저장할거={
      member: [결과.작성자, 요청.user.id],
      date: new Date(),
      title : 요청.params.id
    }
      db.collection("chatroom").insertOne(저장할거, function(에러,결과){

    })

  })
  console.log('채팅방 개설 완료!')
  응답.redirect('/chat/'+게시글번호)
})
  
