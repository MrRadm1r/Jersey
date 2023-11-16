let bg, player, astr_1, astr_2, astr_3, mgbg_1, canister, fail_bg, flower_room, flowers, water1, water2, done;
let mySound, theme, gasf;
let w = window.innerWidth;
let h = window.innerHeight;
let game = true;
let xpos = 0;
let ypos = 0;
let mgopen = false;
let mov = [0, 0];
let pos = [0, 0];
let speed = 5;
let stamina = 0.7;
let objs = [];
let over = 0;
let plwidth = 90;
let plheight = 140;
let mg2w = 100
let mg2h = 100
let mg2x = w * 0.25
let mg2y = 0
let mgw = w * 12 / 14;
let mgh = w * 12 / 14;
let mgx = w / 14;
let mgy = h / 14;
let isHan = false;
let overbox = false;
let full = [0];
let plants = [[w * 0.25, h * 0.5, 100, h * 0.5], [w * 0.5, h * 0.5 - h * 0.25, 100, h * 0.75], [w * 0.75, h * 0.5, 100, h * 0.5]];
let activeSprite;
let playerr;
let playerl;
let playerd;
let a = 0;
let oxygen = 0.55;
let border = 150;
let gaslvl = 0;
let countDown = [150, 100, 100];
let waterlvl = 0;
let flower_astr;
let fuel_astr;

//let is = 0;


function preload() {
  // изображения
  bg = loadImage("img/bg.png")
  player = loadImage("img/player.png")
  astr_1 = loadImage("img/asteroid_1.png")
  astr_2 = loadImage("img/asteroid_2.png")
  astr_3 = loadImage("img/asteroid_3.png")
  mgbg_1 = loadImage("img/fuel.png")
  canister = loadImage("img/canister.png")
  playerr = loadImage("img/playerr.png")
  playerl = loadImage("img/playerl.png")
  playerd = loadImage("img/playerb.png")
  fail_bg = loadImage("img/fail_bg.png")
  flower_room = loadImage("img/flower_room.png")
  flowers = loadImage("img/flowers.png")
  done = loadImage("img/done.png")
  water1 = loadImage("img/water1.png")
  water2 = loadImage("img/water2.png")
  flower_astr = loadImage("img/flowers_astr.png")
  fuel_astr = loadImage("img/asteroid_fuel.png")
  /*flower_astr = loadimage("img/asteroid_flower.png")
  fuel_astr = loadimage("img/flowers_astr.png")
  flower_astr, fuel__astr,*/

  fire = [loadImage('img/fire/fire1.png'),loadImage('img/fire/fire2.png'),loadImage('img/fire/fire3.png')]
  fireRev = [loadImage('img/fire/fired1.png'),loadImage('img/fire/fired2.png'),loadImage('img/fire/fired3.png')]


  // звуки
  soundFormats('mp3', 'ogg');
  mySound = loadSound('sounds/mg_open.mp3');
  theme = loadSound('sounds/theme.mp3');
  gasf = loadSound('sounds/liq.mp3');
}



class Collision {
  constructor(posx, posy, width, height) {
    this.posx = posx
    this.posy = posy
    this.width = width
    this.height = height
  }
  isCollision(plposx, plposy, range) {
    if (plposx > this.posx - this.width - range + (this.width - plwidth) / 2
      && plposx < this.posx + this.width + range - (this.width - plwidth) / 2
      && plposy > this.posy - this.height - range + (this.height - plheight) / 2
      && plposy < this.posy + this.height + range - (this.height - plheight) / 2) {
      return true;
    }
    else {
      return false;
    }
  }
}


function crtobj(x, y, limg) { // Рисует объекты и создаёт им коллизии
  x -= pos[0]
  y -= pos[1]
  image(limg, x, y)
  objs.push(new Collision(x + limg.width / 3, y + limg.height / 3, limg.width, limg.height))
}

// МИНИ
// ИГРА
function minigame(name) { // Мини-игра. аргрумент - номер игры.
  imageMode(CENTER)
  
  if (name == 1) {
    image(mgbg_1, w / 2, h / 2, w / 14 * 12, h / 14 * 12)
    image(canister, w / 2.05, h / 1.47, canister.width / 14 * 8, canister.height / 14 * 8)
    fill(255, 0, 0)
    noStroke()
    ellipse(w / 3.25, h / 1.7, h / 8)
    if (dist(w / 3.25, h / 1.7, mouseX, mouseY)<h/16 && mouseIsPressed){
      fill(200, 0, 0)
      ellipse(w / 3.25, h / 1.7, h / 8)
      if (!gaslvl){
          gasf.play()
      }
      gaslvl++;
    }
    
    
    imageMode(CORNER)


    // ВТОРАЯ МИНИ ИГРА
  } else if (name == 2) {
    imageMode(CENTER)
    rectMode(CORNER)
    image(flower_room, w/2, h/2, w*12/14, h*12/14)
    overbox = mouseX > mg2x - mg2w && mouseX < mg2x + mg2w && mouseY > mg2y - mg2h && mouseY < mg2y + mg2h
    
    noStroke()

    fill(255 - 255 * full[0], 255 * full[0], 0)
    //rect(width * 0.25, height * 0.75 - (w + h) / 57 * 2, width * 0.5, height * 0.25)
    image(flowers, width/2, height/2+height/10, width * 0.5 / 4*3, flowers.height*(width * 0.5/flowers.width) / 4*3)
    

    fill(255)

    rectMode(CENTER)
    if (isHan) {
      if(!mouseIsPressed)
        image(water1, max(min(mouseX, width - mg2w / 2), mg2w / 2), max(mg2h / 2, min(mouseY, height - mg2h / 2)), mg2w*2, mg2h*2)
      else 
        image(water2, max(min(mouseX, width - mg2w / 2), mg2w / 2), max(mg2h / 2, min(mouseY, height - mg2h / 2)), mg2w*2, mg2h*2)
        waterlvl++;
    }
    else {
      image(water1, mg2x, mg2y, mg2w*2, mg2h*2)
    }

    if (isHan && mouseIsPressed) {
      for (let i = 0; i < plants.length; i++) {
        if (mouseX > plants[i][0] - plants[i][2] && mouseX < plants[i][0] + plants[i][2] && mouseY > plants[i][1] - [3] && mouseY < plants[i][1] + plants[i][3]) {
          if (full[i] < 1) { full[i] += 0.01 }
        }
      }
      
    }
  }
  
  strokeWeight((w + h) / 57)
  stroke(128)
  fill(0, 0)
  rectMode(CORNER)
  rect(w / 14, h / 14, w / 14 * 12, h / 14 * 12, (w + h) / 75)
}


function mousePressed() {
  if (overbox && !isHan) {
    isHan = true
  }
}


function setup() {
  frameRate(60)
  createCanvas(w, h);
  pos = [width * 0.5 - 50, height * 0.5 - 50]
  isHan = false
  overbox = false
  full = [0]
  plants = [[width * 0.25, height * 0.75 - (w + h) / 57 * 2, width * 0.5, height * 0.25]]
  mg2y = height * 0.75 - (w + h) / 57 * 2 + mg2h * 2
  activeSprite = player
  theme.play();
  theme.loop();
}

//////

function draw() {
  if (game){
  
  if (mgopen == false) {
    mov[1] = keyIsDown(83) * speed - keyIsDown(87) * speed // S W
    mov[0] = keyIsDown(68) * speed - keyIsDown(65) * speed // D A

    if (keyIsDown(65)) {
      activeSprite = playerl
    }
    if (keyIsDown(68)) {
      activeSprite = playerr
    }
    if(keyIsDown(83)) {
      activeSprite = playerd
    }

    if (!keyIsDown(65) && !keyIsDown(68) && !keyIsDown(83)) {
      activeSprite = player
    }
  }

  imageMode(CORNER)
  image(bg, -pos[0], -pos[1], w * 2, h * 2);
  rectMode(CENTER)
  if (pos[0] <= 0) {
    pos[0] = 0  
  }
  if (pos[1] <= 0) {
    pos[1] = 0
  }
  if (-pos[0] <= -w) {
    pos[0] = w
  }
  if (-pos[1] <= -h) {
    pos[1] = h
  }


  // ФОН
  speed = 5;
  // проверка коллизий
  for (let i of objs) {
    if (i.isCollision(w / 2, h / 2, 0)) {
      if (i.posy - pos[1] > 0 && Math.abs(i.posy - pos[1]) > Math.abs(i.posx - pos[0])) {
        pos[1] -= speed
      } else if (i.posy - pos[1] < 0 && Math.abs(i.posy - pos[1]) > Math.abs(i.posx - pos[0])) {
        pos[1] += speed
      } else if (i.posx - pos[0] > 0 && Math.abs(i.posy - pos[1]) < Math.abs(i.posx - pos[0])) {
        pos[0] -= speed
      } else if (i.posx - pos[0] < 0 && Math.abs(i.posy - pos[1]) < Math.abs(i.posx - pos[0])) {
        pos[0] += speed
      }
    }
  } // конец

  if (a>=20) {
    a = 0
  }
  else {
    a++
  }

  noStroke()
  fill(255)
  fill(255, 0, 0)
  imageMode(CENTER)
  image(activeSprite, w / 2, h / 2, 90, 140) // player
  pos = [pos[0] + mov[0], pos[1] + mov[1]] //player posissions
  if(!mgopen) {
    if(activeSprite == playerl) {
      image(fire[Math.floor(a/10)],w/2-(-20),h/2+50,20,40)
    }
    else if(activeSprite == playerr) {
      image(fire[Math.floor(a/10)],w/2-(20),h/2+50,20,40)
    }
    else if(activeSprite == playerd) {
      image(fireRev[Math.floor(a/10)],w/2,h/2-50,30,60)
    }
  }

  imageMode(CORNER)
  // удаление устаревших элементов из списка
  objs.pop()
  objs.pop()
  objs.pop()// конец
  crtobj(w - w / 7, h / 2, fuel_astr)
  crtobj(w + w / 5, h - h / 4, flower_astr)
  crtobj(w / 2, h / 1, astr_2)


  // Стамина
  fill(255, 100*(stamina) , 0).rectMode(CORNER)
  rect(border, border + 160 - 160 * stamina, 70, 160 * stamina)
  stroke(255)
  strokeWeight(5)
  fill(0, 0, 0, 0)
  rect(border, border, 70, 160)

  noStroke()
  fill(0,128,166)

  // Кислород
  rect(border+100, border + 160 - 160 * oxygen, 70, 160 * oxygen)
  stroke(255)
  strokeWeight(5)
  fill(0, 0, 0, 0)
  rect(border+100, border, 70, 160)

  oxygen -= 0.0001


  // стамина-бар    
  if ((keyIsDown(87) || keyIsDown(83) || keyIsDown(65) || keyIsDown(68)) && stamina > 0) {
    stamina -= 0.0005
    // конец
  }
  // открытие мини-игры
  if (objs[0].isCollision(pos[0], pos[1], 200) && (keyIsDown(70) || mgopen)) {
    if (mgopen == false) {
      mySound.play();
    }
    mgopen = true
    minigame(1)
  } else if (objs[1].isCollision(pos[0], pos[1], 200) && (keyIsDown(70) || mgopen)) {
    if (mgopen == false) {
      mySound.play();
    }
    mgopen = true
    minigame(2)
  }
  if (keyIsDown(27)) {
    mgopen = false
  } // конец
  if (stamina<=0 || oxygen<=0){
    game = false
  }
  rectMode(CENTER)
  if (gaslvl>=160 && countDown[0]>0){
    image(done, w/2, 0)
    console.log(w)
    countDown[0]--
    if (stamina<=1){
      stamina += 0.003
    }
    
  }
  if (waterlvl>=150 && countDown[1]>0){
    imageMode(CORNER)
    console.log(w)
    image(done, width/2, 0)
    countDown[1]--
  }
  /*
  if (gaslvl>=50 && countDown[2]>0){
    image(done, w/2, 0)
    countDown[2]--
  }*/


}
else{
  tint(255, 255, 255, 5)
  image(fail_bg, 0, 0, w, h);
}
}