function statusUpdate() {
	var counter = 0;
	stream = db.stream.find({status: {'$exists':1} }).limit(300000);
	
	stream.forEach(function(d){
		counter = counter + 1;
		d.st = {
			"ln": parseInt(d.status[0]),
			"lc": parseInt(d.status[1]),
			"pl": parseInt(d.status[2])
		};
		delete d['status']
		print(counter)
		db.stream.save(d)
	})
}
statusUpdate()



stream = db.temp.update({status: "000"}, {$unset:{status:""}, $set:{st:{ln:0,lc:0,pl:0}} } );

db.stream.update({status: "000"}, {$unset:{status:""}, $set:{st:{ln:0,lc:0,pl:0}} }, {multi:true} );
db.stream.update({"st.pl":0, lang: {$ne: "tr"} }, {$set:{ "st.pl":4, "st.ln":1 } }, {multi:true});
db.stream.findOne({_id:ObjectId("52dacf3b841f8cd1738b47f3"),"st.pl":0, lang: {$ne: "tr"} });
