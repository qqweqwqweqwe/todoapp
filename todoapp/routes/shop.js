var router=require('express').Router(); // 라우터 만드는법

function 로그인했니(요청,응답,next){
  if(요청.user){  //로그인후 세션이 있으면 항상 요청.user 가 있음
    next()   // 로그인 한 상황이면 그 다음으로 보내줌
  }
  else{
    응답.send('로그인 안하셨는데요?')
  }
}

router.use(로그인했니) // 여기있는 모든 url에 적용할 미들웨어

router.get('/shirts', 로그인했니,function(요청,응답){  // 로그인 한 사람만 들어가게 해주려면 중간에 미들웨어 추가해야함 
  응답.send('셔츠 파는 페이지 입니다')
})

router.get('/pants', function(요청,응답){
  응답.send('바지 파는 페이지입니다')
})

module.exports = router