from flask import Flask, request
app = Flask(__name__)


HTML_START = '''
            <form method = 'POST' action ='/'>
                <p>Keep in mind one number in range from 0 to 1000</p>
                <p>I'll guess in 10 steps what number it is</p>
                <input type='submit' value='ok'>
                <input type='hidden' name='min' value='{}'>
                <input type ='hidden' name='max' value='{}'>  
                <input type ='hidden' name='guess' value='{}'>     
            </form>        
            '''

HTML_PLAY = '''
            <form method = 'POST' action = '/'>
            <p>My guess is {guess}<p>
                <input type='submit' name='ans' value='Too big'>
                <input type='submit' name='ans' value='Too small'>
                <input type='submit' name='ans' value='You won'>
                <input type='hidden' name='min' value='{min}'>
                <input type='hidden' name='max' value='{min}'>
                <input type='hidden' name='guess' value='{guess}'>
            </form>
            
            '''
HTML_END =  '''
            <p>Your number is {guess}</p>
            Thanks for a good fun!
            '''

HTML_LIER = '''
            <form method = 'POST' action = '/'>
            You're lying to me 
            </form>
            '''
@app.route('/', methods=['GET', 'POST'])
def guessing():
    if request.method == 'GET':
        ans = '0'
        return HTML_START.format(0, 1000, 500)
    else:
        min = int(request.form.get('min'))
        max = int(request.form.get('max'))
        ans = request.form.get('ans')
        guess = int(request.form.get('guess'))
        if ans == 'You won':
            return HTML_END.format(guess=guess)
        elif ans == 'Too big':
            max = guess
        elif ans == 'Too small':
            min = guess
        if min == max:
            return HTML_LIER.format()
        guess = (max - min) // 2 + min
        return HTML_PLAY.format(guess=guess, min=min, max=max)

if __name__ == '__main__':
    app.run()