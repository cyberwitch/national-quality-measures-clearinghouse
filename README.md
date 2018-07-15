# National Quality Measures Clearinghouse
On July 16, 2018, the National Quality Measures Clearinghouse at
https://www.qualitymeasures.ahrq.gov/ will no longer be accessible,
due to federal funding cuts.  In an attempt to prevent this wealth
of medical knowledge from being lost, I have tried to backup as
much of the raw data as possible before it is gone.  It is my hope
that I (or individuals with more knowledge of medical practice than
I) can recreate the original search and cross-reference tools.

## Summaries
The bulk of NQMC data appears in what are called summaries.  I have
been unable to access the archive page listing all summaries due to
server timeouts (I am sure I am not the only archivist today), and
so I wrote a script that attempts to download every summary by
iterating through possible ids.  I don't know what all the files
are for, but the information-dense guidelines of care seem to be
the files larger than 8kB, or those with a `Title`
(`FieldID="11"`.)

The downloaded files are in an xml format that was provided for
general use.  I believe importing them into a new database will be
a task relatively easily accomplished, especially with the help of
http://archive.org/ to show how information was presented
originally.

# Commentaries
These are expert commentaries on the quality measures.  With no xml
output, I have simply saved all in their original html.  Hopefully
they can be parsed for easier viewing and searching, and links to
the summaries in question restored.
