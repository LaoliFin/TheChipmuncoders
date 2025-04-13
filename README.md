# TheChipmuncoders
## TITLE
Folkify

## ABOUT
Our project is a website called FOLKIFY that creates digital greeting cards in a fun and innovative way. The user inputs a personal message they want to send to someone, and our app transforms it into a musical experience by generating a song based on real traditional Irish folk melodies.

In addition to the music, the app also generates a personalized digital greeting card. It includes a summarized version of the original message along with an AI-generated image that reflects the tone or theme of that summary. Both the song and the card can be downloaded and shared.

## TECH STACK
The main coding languages we used are python, html with some JavaScript and css. Our backend uses Flask. For retrieving the melodies we used the database [the session](https://thesession.org/) API. We also used many python libraries, such as [music21](https://music21-mit.blogspot.com/). Beside that we have also used [midi2voice](https://github.com/mathigatti/midi2voice) for generating singing. The image prompts were generated with Gemini's text generator and the subsequent images were created by feeding the prompt to Gemini's image generator. We also the Roo extension in VS Code to help us with html formatting and debugging.

## FEATURES
The main feature is generating Irish folk-style songs using the user’s custom message as lyrics. 
Besides that it creates a downloadable digital card with a summary of the message and an AI-generated image based on that summary.It also includes optional voice filters like choir and chipmunks

## SETUP
To run the server locally:
- midi2voice requires [MuseScore3](https://musescore.org/en/download) to be installed on the computer
- to insure all python libraries are installed use: pip install -r requirements.txt in the root directory
- run the server by typing: python (or py) app.py
- open the correct port in your preferable browser
- enjoy the chaos :D
  
To use our web-app:
- Go to the website URL
- Input your message in the left text field.
- Choose a genre of folk song or let it select one at random.
- (Optional) Pick a voice filter — current options include choir and chipmunks.
- When you’re happy with the input and settings, click the GENERATE button.
- Wait a moment while the song is being created.
- Listen to your song and enjoy a fun animation.
- Click DOWNLOAD to save the song.
- Click GO TO CARD to view the generated card.
- Turn the card using the page turner in the bottom-right corner.
- Click DOWNLOAD to save the full greeting card (image + song).



## USAGE
This web app can be used in a variety of creative and meaningful ways, such as:
- Sharing good news in a fun and unique style
- Making bad news a little easier to deliver, with a touch of music
- Turning emails or study notes into songs to make them less boring
- Simply having fun with friends 

## CHALLENGES & LEARNING
We practiced and improved our Python, HTML, and CSS skills, learned how to build a song generator using MIDI files, we became better at researching and integrating useful libraries and online resources and we gained experience in combining AI-generated content with interactive design.

## FUTURE IMPROVEMENTS
In the future we would make the post-production of the song better by adding voice options (male/female) and allowing user to adjust tempo and pitch. We would also introduce premium accounts that would have extended generation limits.



