# Trying to find structure

In this folder I'm gathering the data and my thoughts in order to create, to the
best of my ability, the most practically useful structure for navigation and
overview of this documentation.

## Early thoughts

The list of tags has a count, telling us how many pages have each tag. This is a
very rough measure of breadth and importance, or perhaps a measure of how messy
our documentation has become.

It might be *very* enlightening to have some usage statistics. What pages are
people visiting, what topics are people searching for, what are they asking the
chatbot about?

Then again, it is not just the most often looked up pages that need to be easy
to find. Sometimes things we do only once are the most important.

## Later thoughts

In addition to the list of tags, I've used the list of topics from Marzieh's
AI-wiki experiment, with the count of how many sources each topic refers to. The
sources in there are one-to-one with pages of the documentation except for a bug
where filenames that exist in multiple locations get confused into one source.

And, perhaps most usefully, I did sit down and write any and all categories that
came to mind - these are at the top of the file potential-groupings.md.

I compiled those three sets of categories into one large list, and pulled out
the index of sources with one-line summaries from the AI-wiki, with the plan of
feeding those two files to an LLM to see what structure it would suggest. I have
not attempted this yet.

## Structure attempt one

Instead of feeding an LLM, this was created by my brain. After looking at all of
this, and the current file structure, and the current website structure.

For now it is in the file structure-attempt-one.txt.

The next step is to attempt sorting all the documentation in that structure and
see what happens. What is hard to sort or ends up in unsorted? Does it become an
easily navigable website? Does it become confusing in some way? What seems to be
missing? What seems to be too much? Which categories need an index.md page and
which ones don't?
