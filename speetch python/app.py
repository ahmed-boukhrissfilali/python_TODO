from gtts import gTTS 

# data 
data  = "hi my name is ahmed welcom to my  speeker en english "

lange = "en"

#audio prepare 

res = gTTS(text=data , lang=lange)


#save audio
res.save("audio.mp3")