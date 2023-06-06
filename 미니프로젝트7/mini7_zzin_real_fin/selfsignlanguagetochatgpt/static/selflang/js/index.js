function showImage(file, dropZone) {
    const reader = new FileReader();

    reader.onload = function(e) {
      const image = document.createElement('img');
      image.src = e.target.result;

      dropZone.innerHTML = '';
      dropZone.appendChild(image);
    };

    reader.readAsDataURL(file);
  }
function setupDropZone(dropZone, fileInput) {
    dropZone.ondrop = function(e) {
        e.preventDefault();
        this.className = 'drop-zone';

        fileInput.files = e.dataTransfer.files;
        showSelectedFiles(fileInput.files); // 추가: 파일 출력 함수 호출

        // 추가: 이미지 표시
        for (let i = 0; i < fileInput.files.length; i++) {
            showImage(fileInput.files[i], this);
        }
    }

    dropZone.ondragover = function() {
        this.className = 'drop-zone drop';
        return false;
    }

    dropZone.ondragleave = function() {
        this.className = 'drop-zone';
        return false;
    }
}

function showSelectedFiles(files) {
    const fileContainer = document.getElementById('file-container');
    fileContainer.innerHTML += "<br>"; // 기존 파일 출력 내용 초기화

    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const fileElement = document.createElement('div');
        fileElement.textContent = file.name;
        fileContainer.appendChild(fileElement);
    }
}

document.addEventListener("DOMContentLoaded", function() {
    let dropZone = document.getElementById('drop_zone-0');
    let fileInput = document.getElementById('file-input-0');
    setupDropZone(dropZone, fileInput);
}, false);

let idNum = 0;
function addFile() {
    deepCopy();
}

function deepCopy()  {
    idNum++;
    const fileModule = document.getElementById('file-module-0');

    // 노드 복사하기 (deep copy)
    const newNode = fileModule.cloneNode(true);

    // 복사된 노드의 id 변경하기
    newNode.id = 'file-module-' + idNum;
    const dropZone = newNode.querySelector('#drop_zone-0');
    dropZone.id = 'drop_zone-' + idNum;
    const fileInput = newNode.querySelector('#file-input-0');
    fileInput.id = 'file-input-' + idNum;

    // 이벤트 핸들러 설정하기
    setupDropZone(dropZone, fileInput);

    // 복사한 노드 추가하기
    fileModule.after(newNode);
}