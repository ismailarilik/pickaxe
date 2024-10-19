# pickaxe

This project aims to be built to a text editor.
Its main goal is actually editing code but code is also a text so I prefer that more general title.
As a result, most users would be developers.
Because of that, it will support features to make development easier such as syntax highlighting, code completion and debugging.
You can think that code completion and debugging are generally IDE features and an editor shouldn't have them.
But they are really useful features for big projects and can be included in a lightweight editor.
To be able to keep the lightweight nature, these features will be added as extensions.

It is written using literate programming.
So all project is actually a book.
You can read it, and find and fix typos or bugs in it.
It is a document both humans and computers can understand.

I wanted to write it this way because I realized that the best way to develop a well-organized project is practicing TDD.
When I tried to write tests before the implementation, I noticed that tests are like specification of implementation.
They are, of course, code.
But function names for these tests are like some rules only humans can understand; they mean nothing to computers.
But these function names were too short and confusing so I needed to add some comments above the functions.
These comments were prone to be a document.
But they are just ordinary comments.
I couldn't add a title, a list or an image to them so they were also confusing.
Then I thought what would happen if I try to practice _literate programming_ in this project.
So the journey has begun.

Literate programming makes sense for any project because we are _thinking_ this way.
We worked hard to develop programming languages which were similar to our speaking languages and our thinking processes.
Because we are thinking and express ourselves that way.
But the gap between our thoughts and languages, and programming languages is still big.
Nevertheless we continue to put our early thoughts directly into code.
We can use _literate programming_ to make our thoughts mature, organized and right, then we can write code with peace of mind.
Here I've just tried this.
