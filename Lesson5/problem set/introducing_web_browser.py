# Introducing Your Web Browser 
#
#
# Although we have not put our HTML interpreter and our JavaScript
# interpreter together yet, we can still render HTML-only web pages. 
#
# A critical concept in interpreting HTML is proper tag nesting. 
#
# In this exercise you will learn a bit of HTML on your own and construct
# properly nested, simple HTML that renders to match the reference image we
# have provided. You do not have to match the exact text shown, but you do
# have to match the order and nesting of the tags used. 
#
# See the rendering image for reference output.
#
# In class we have discussed a few HTML tags, such as <b>, <i>, 
# <a href="http://www.udacity.com">, and <p>. It turns out, there are many
# more. In this exercise you will reverse-engineer some HTML tags you may
# not have seen before. Explicitly teaching you the various HTML tags is
# not a focus of this course, but you now know enough to learn them 
# easily on your own.
#
# Complete the webpage string below with HTML that renders an image similar
# to the reference. You must match the tag ordering and nesting, but you
# can change the text. 
#
# The reference image explicitly names every HTML tag it uses (it puts them
# in parentheses instead of angle brackets). If you would like a bit of a
# challenge, you can infer everything from that image alone. However, you
# are also encouraged to use any external source or HTML tutorial you would
# like. For example, these may help you brush up: 
# 
# http://www.w3schools.com/html/html_primary.asp
# http://www.w3schools.com/html/html_elements.asp
# http://www.w3schools.com/html/html_headings.asp
# http://www.w3schools.com/html/html_lists.asp 
# http://www.w3schools.com/html/html_images.asp
#
# Hint 1: The most common error is <b> opening one tag then </u> closing
# another. For our web browser, even tags like <p>, <li> and <img> must be
# properly closed! (Real-world web browsers are more forgiving, but one
# purpose of this exercise is to master properly nested tags.)
#
# Hint 2: Unlike <a href=...>my text</a>, do not put any text inside 
# <img src=...></img>. Just close it immediately. 

webpage = """<html>
<h1>Level One Headings Use (H1) Tags</h1> 
<p>Paragraphs use (P) tags. Unordered lists use (UL) tags.
<ul>
  <li> List items use (LI) tags.</li> 
  <li> Text can be <b>bold (B)</b>, <i>italic (I)</i>, <small>small (SMALL)</small>, <big>big (BIG)</big>, or look like a <tt>typewriter (TT)</tt>. </li>
  <li> There are also ordered lists that use (OL) tags. Let's make one nested inside our current list item.
   <ol>
   <li> Text can also be <strong>strong (STRONG)</strong> or <em>emphasized (EM)</em>, which typically renders like bold and italics.</li>
   <li> Webpages can have <a href="http://www.google.com">hyperlinks (A HREF="target")</a>.</li>
   </ol>
  </li>
  <li> It is also possible to include images <img src="cs262.png"> </img> (IMG SRC="cs262.png")
  </li>
</ul>
</p> 
<p>
We'll finish off with one last paragraph.
</p>
</html>
"""

# Display the page!

import ply.lex as lex
import ply.yacc as yacc
import htmltokens
import htmlgrammar
import htmlinterp
import graphics as graphics
import jstokens


htmllexer = lex.lex(module=htmltokens) 
htmlparser = yacc.yacc(module=htmlgrammar,tabmodule="parsetabhtml") 
ast = htmlparser.parse(webpage,lexer=htmllexer) 
jslexer = lex.lex(module=jstokens) 
graphics.initialize() # Enables display of output.
htmlinterp.interpret(ast) 
graphics.finalize() # Enables display of output.