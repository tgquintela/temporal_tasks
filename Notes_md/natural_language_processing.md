
#Natural language processing
2016-06-01

Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics which tries the understand human (natural) languages. It is a field strongly related with human-computer interaction, computational linguistics.

The main tasks related with NLP are:
* _Automatic summarization_: produce a readable summary of a chunk of text. Often used to provide summaries of text of a known type, such as articles in the financial section of a newspaper.
* _Coreference resolution_: given a sentence or larger chunk of text, determine which words ("mentions") refer to the same objects ("entities"). Anaphora resolution is a specific example of this task, and is specifically concerned with matching up pronouns with the nouns or names that they refer to. 
* _Discourse analysis_: this rubric includes a number of related tasks. One task is identifying the discourse structure of connected text, i.e. the nature of the discourse relationships between sentences (e.g. elaboration, explanation, contrast). Another possible task is recognizing and classifying the speech acts in a chunk of text (e.g. yes-no question, content question, statement, assertion, etc.).
* _Machine translation_: automatically translate text from one human language to another one. This is one of the most difficult problems, it is include in a group termed colloquially as "AI-complete" problem. That's means that required not only the text but also the knowledge that humans possess as grammar, semantics, facts about the real world.
* _Morphological segmentation_: separate words into individual morphemes and identify the class of the morphemes. The difficulty of this task depends greatly on the complexity of the morphology (i.e. the structure of words) of the language being considered. English has fairly simple morphology, especially inflectional morphology, and thus it is often possible to ignore this task entirely and simply model all possible forms of a word (e.g. "open, opens, opened, opening") as separate words.
* _Named entity recognition_ (NER): given a stream of text, determine which items in the text map to proper names, such as people or places, and what the type of each such name is (e.g. person, location, organization). Note that, although capitalization can aid in recognizing named entities in languages such as English, this information cannot aid in determining the type of named entity, and in any case is often inaccurate or insufficient.
* _Natural language generation_: convert information from computer databases into readable human language.
* _Natural language understanding_: convert chunks of text into more formal representations such as first-order logic structures that are easier for computer programs to manipulate. Natural language understanding involves the identification of the intended semantic from the multiple possible semantics which can be derived from a natural language expression which usually takes the form of organized notations of natural languages concepts.
* _Optical character recognition_ (OCR): given an image representing printed text, determine the corresponding text.
* _Part-of-speech tagging_: given a sentence, determine the part of speech for each word. Many words, especially common ones, can serve as multiple parts of speech. Some languages have more such ambiguity than others. Languages with little inflectional morphology, such as English are particularly prone to such ambiguity. Chinese is prone to such ambiguity because it is a tonal language during verbalization. Such inflection is not readily conveyed via the entities employed within the orthography to convey intended meaning.
* _Parsing_: determine the parse tree (grammatical analysis) of a given sentence. The grammar for natural languages is ambiguous and typical sentences have multiple possible analyses, some of them without any sense for humans.
* _Question answering_: given a human-language question, determine its answer. There are questions with close answer but others are open-ended questions which are more difficult to answer.
* _Relationship extraction_: given a chunk of text, identify the relationships among named entities (e.g. who is married to whom).
* _Sentence breaking_ (also known as sentence boundary disambiguation): given a chunk of text, find the sentence boundaries. Sentence boundaries are often marked by periods or other punctuation marks, but these same characters can serve other purposes.
* _Sentiment analysis_: extract subjective information usually from a set of documents, often using online reviews to determine "polarity" about specific objects. It is especially useful for identifying trends of public opinion in the social media, for the purpose of marketing.
* _Speech recognition_: given a sound clip of a person or people speaking, determine the textual representation of the speech. This is the opposite of text to speech and is one of the extremely difficult problems colloquially termed "AI-complete". In natural speech there are hardly any pauses between successive words, and thus speech segmentation is a necessary subtask of speech recognition. Note also that in most spoken languages, the sounds representing successive letters blend into each other in a process termed coarticulation, so the conversion of the analog signal to discrete characters can be a very difficult process.
* _Speech segmentation_: given a sound clip of a person or people speaking, separate it into words. A subtask of speech recognition and typically grouped with it.
* _Topic segmentation and recognition_: given a chunk of text, separate it into segments each of which is devoted to a topic, and identify the topic of the segment.
* _Word segmentation_: separate a chunk of continuous text into separate words.
* _Word sense disambiguation_: many words have more than one meaning; we have to select the meaning which makes the most sense in context. For this problem, we are typically given a list of words and associated word senses, e.g. from a dictionary or from an online resource such as WordNet.
* _Information retrieval_ (IR): this is concerned with storing, searching and retrieving information. It is a separate field within computer science (closer to databases), but IR relies on some NLP methods (for example, stemming). Some current research and applications seek to bridge the gap between IR and NLP.
* _Information extraction_ (IE): this is concerned in general with the extraction of semantic information from text. This covers tasks such as named entity recognition, Coreference resolution, relationship extraction, etc.
* _Speech processing_: this covers speech recognition, text-to-speech and related tasks.

***Tags***: Computer science, Data Analysis, Artificial Intelligence

#### See also
[Computational intelligence](/computational_intelligence), [Mathematical optimization](/mathematical_optimization), [Computer vision](/computer_vision), [Artificial Intelligence](/artificial_intelligence), [Data Analysis](/data_analysis), [Machine Learning](/machine_learning)
## Material
* http://research.google.com/pubs/NaturalLanguageProcessing.html
* http://www.nltk.org/

## Papers
* Bates, M (1995). [Models of natural language understanding](http://www.pnas.org/content/92/22/9977). Proceedings of the National Academy of Sciences of the United States of America 92 (22): 9977-9982

## Books
* Manning, Christopher D.; Schütze, Hinrich (1999). [Foundations of Statistical Natural Language Processing](https://www.goodreads.com/book/show/776349.Foundations_of_Statistical_Natural_Language_Processing). MIT Press (MA)
* Jurafsky, Dan; Martin, James H. (2000). [Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics and Speech Recognition](https://www.goodreads.com/book/show/908047.Speech_and_Language_Processing). Prentice Hall
* Bird, Steven; Klein, Ewan; Loper, Edward (2009) [Natural Language Processing with Python](https://www.goodreads.com/book/show/6392569-natural-language-processing-with-python). O'Reilly Media


