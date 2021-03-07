function download_btn(){
	// get video link
	video_link = document.getElementById("video-link").textContent;
	console.log(video_link);
	
	const toSend = {
		link: video_link,
		value: "Download"
	};

	const jsonString = JSON.stringify(toSend);
	const xhr = new XMLHttpRequest();

	xhr.open("POST", '/json');
	xhr.setRequestHeader("Content-type", "application-json");
	xhr.send(jsonString);
	console.log('JSON sent.');
}