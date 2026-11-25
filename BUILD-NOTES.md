Build notes for the Tell a Whole Story in 32 Characters entry.

The idea started from the judge brief. A Wi-Fi name only works if a stranger
gets the joke on the first read, so the entry had to be a situation, not a
punchline that needs a setup. A divorce came to mind because it is a story
everyone already knows the shape of: two people, a split, and somebody
walking out with something. The twist is what they walked out with. A router
is the one household object whose loss is felt instantly and constantly, and
putting it ahead of the children flips the expected order of what matters in
a breakup. That inversion is the whole joke, and it is also the whole story:
she left, she chose the router over the kids, and the narrator is now the one
staring at the network list with the children and no internet.

Earlier candidates were weaker. A name about a dad changing the password
again was a situation but had no twist, just a complaint. A name about the
router filing for divorce gave the router a personality but no human story
behind it. A name about a partner leaving for the faster band was cute but
the story ended at the joke, with nothing left for the reader to fill in.
The chosen line keeps a person, a choice, and a consequence in twenty-six
characters, and every word earns its place.

The program itself is deliberately small. It holds one fixed line, checks it
against the one to thirty-two character gate before writing, and writes it
to the output path with no trailing newline. There is no network use, no
input file, and nothing random. Verification was done by running the program
fresh, reading the output file back, counting the characters by hand twice,
and computing the hash of the file both with and without a trailing newline
so the two values could be compared honestly.
