var router=require('express').Router(); // 라우터 만드는법

router.get('/sub/sports', function(요청,응답){  //
  응답.send('스포츠 게시판')
})

router.get('/sub/game', function(요청,응답){
  응답.send('게임 게시판')
})

module.exports = router   // 다른곳에서 이 파일 가져다 쓸대 내보낼 변수 