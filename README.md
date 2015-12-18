<h4>LOGIC:</h4>
<p>The program is a basic user input and file output operation. The user is presented with some options to choose
and these are stored in a series of strings and arrays that are used to create a ringtone. Only one reason and one
ending may be chosen.</p>

<h4>MODES:</h4>
<h5>Interactive:</h5>
<p>This first presents the user with some statements to choose from, regarding gender, phone number, reason for the
voicemail, ending for the voice mail, file save name and whether or not they would like to add a jingle. These
responses are then used to download corresponding MP3 files and stitch the the final ringtone together. The
responses are also saved to a text document using the same file name that the user inputted earlier.</p>
<h5>Command Line:</h5>
<p>This mode requires the user to enter in the variables (gender, phone number, reason, ending, jingle, output name)
into the command line. The application will detect this form of input and pass the variables directly into the
stitchMP3 function, creating the ringtone file.</p>
<p>In both modes, the downloaded files used to stitch the ringtone will be deleted before the program exits. Only
one reason and ending may be chosen in either mode</p>

<h4>USAGE:</h4>
<h5>Interactive</h5>
<p>The program will automatically boot into interactive mode. Follow on-screen instructions to create a ringtone.
Only one reason and one ending may be chosen.</p>
<h5>Command Line:</h5>
<p>Using the command line, you can add the following keywords to the end of the filename to create a ringtone
directly. Only one reason and one ending may be chosen.</p>
<ul>
<li>-g: Gender (M/F)</li>
<li>-p: Phone number (10 digit, numeric)</li>
<li>-r: Reasons (numeric)</li>
<li>-e: Endings (numeric)</li>
<li>-j: Jingle (Y/N)</li>
<li>-o: Output file name (string)</li>
</ul>

<p>An example of a correctly formatted command line input would be as follows:</br><br/>
main.py -g M -p 2342342342 -r 1 -e 2 -j Y -o myRingTone</br></br>
The gender and jingle inputs must be capital characters. If any of the input values are incorrect, the program will
automatically start in interactive mode.</p>

<h4>VERSION:</h4>
<p>This program was created for Python 2.7 and was tested on OS X 10.11</p.
