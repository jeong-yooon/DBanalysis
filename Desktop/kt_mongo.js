// 실행 단축키 : F6
// create database
use mongo;
db;

// database list
show dbs;

// create document(row)
db.user.insert({name:'andy', age: 29, email: 'andy@gmail.com'});
show dbs;

// server > databases > collections > documents
// collection list
show collections;

// CRUD: create read updata delete
// database, collection(table), document(row) > CRUD

// CREATE collection
db.createCollection('test');
show collections;

// capped : true로 설정 > 최대 용량, 최대 document 설정
// size : 용량 byte : 최소 용량 4096byte
// max : 최대 document 갯수
db.createCollection('info1', {capped: true, size: 500, max: 5})
show collections;

// DELETE collection
db.test.drop();
show collections;

// CREATE documents
db.info.insert([
    {subject: 'python', level: 1},
    {subject: 'css', level: 2},
    {subject: 'js', level: 3},
    {subject: 'scss', level: 4},
    {subject: 'web', level: 5},
    {subject: 'flask', level: 6},
    {subject: 'nginx', level: 7},
    {subject: 'less', level: 4},
]);
show collections;
db.info.find();
db.info.remove({level: 5});

// READ documents : find()
db.info1.find();

// 쇼핑몰
// RDBMS : 고객(아이디, 패스워드, 이름, 주소) : 구매정보(아이디, 상품명, 가격)
// NoSQL : 고객(아이디, 패스워드, 이름, 주소) : 구매정보(아이디, 상품명, 가격, 이름, 주소)

// DELETE documents : remove()
// capped 조건을 걸어준 collection의 document는 삭제X
db.info1.remove({level: 3});

// READ : documents : condition query
// level >= 4
db.info.find({level: {$gte: 4}});
// subject : flask, nginx
db.info.find({subject: {$in: ['flask', 'nginx']}});
// level > 5, subject == nginx
db.info.find({$and: [{subject: 'nginx'}, {level: {$gt: 5}}]});

// READ : documents : projection : select columns
// _id : 예외동작 : 따로 false 설정하지 않으면 무조건 출력
db.user.find({}, {name: true, age: true});
// age 컬럼 제외하고 출력
db.user.find({}, {age: false});
// _id 제외하고 출력
db.user.find({}, {_id: false, name: true, age: true});
// _id 제외한 컬럼에 true, false를 섞어서 사용 X

// 정렬 : sort()
// level : 오름차순 정렬 : 1
db.info.find().sort({level: 1});
// level : 내림차순 정렬 : -1
db.info.find().sort({level: -1});

// 출력 데이터 갯수 제한 : limit()
db.info.find({level: {$lte: 5}}).sort({level: -1}).limit(3);
// 데이터를 스킵해서 출력 : skip()
db.info.find({level: {$lte: 5}}).sort({level: -1}).skip(4);

// UPDATE : documents : update() : $set
db.info.find();
// python < level == 5 : document 1개만 수정
db.info.update({subject: 'python'}, {$set: {level: 5}});
db.info.find();

// python > level == 4 : 여러개의 document 수정
db.info.update(
    {subject: 'python'},
    {$set: {level: 5}},
    {multi: true}
);
db.info.find();

// function
// pagenation function
db.info.find();
var pagenation = function(page, pageblok){
    return db.info.find().skip((page-1)*pageblock).limit(pageblock);
};
pagenation(2, 3);

// create : insert() : [{data1}, {data2}]
// read : find() : (query, projection) : $gt, $and, $in
// update : update() : (query, update data, option) : $set
// delete : drop() : (query)



