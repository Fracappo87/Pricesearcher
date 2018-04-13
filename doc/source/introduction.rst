Introduction
============

Information Retrieval
---------------------
Information retrieval (IR) is the activity of obtaining information resources relevant to an information need from a collection of information resources. Searches can be based on full-text or other content-based indexing. Information retrieval is the science of searching for information in a document, searching for documents themselves, and also searching for metadata that describe data, and for databases of texts, images or sounds.
An information retrieval process begins when a user enters a query into the system. Queries are formal statements of information needs, for example search strings in web search engines. In information retrieval a query does not uniquely identify a single object in the collection. Instead, several objects may match the query, perhaps with different degrees of relevancy.
An object is an entity that is represented by information in a content collection or database. User queries are matched against the database information. However, as opposed to classical SQL queries of a database, in information retrieval the results returned may or may not match the query, so results are typically ranked. This ranking of results is a key difference of information retrieval searching compared to database searching.
Depending on the application the data objects may be, for example, text documents, images, audio, mind maps or videos.
Most IR systems compute a numeric score on how well each object in the database matches the query, and rank the objects according to this value. The top ranking objects are then shown to the user. The process may then be iterated if the user wishes to refine the query.

Model Types
-----------
For effectively retrieving relevant documents by IR strategies, the documents are typically transformed into a suitable representation. For this project the **Vector Space Model** representation has been adopted.

Vector space model
------------------
Vector space model or term vector model is an algebraic model for representing text documents (and any objects, in general) as vectors of identifiers, such as, for example, index terms. It is used in information filtering, information retrieval, indexing and relevancy rankings.
Documents and queries are represented as vectors.

.. math::

   d_j = ( w_{1,j} ,w_{2,j} , \dotsc ,w_{t,j} )\\
   q = ( w_{1,q} ,w_{2,q} , \dotsc ,w_{n,q} )

Each dimension corresponds to a separate term. If a term occurs in the document, its value in the vector is non-zero.
Several different ways of computing these values, also known as (term) weights, have been developed. One of the best known schemes is tf-idf weighting. This is the scheme adopted for ranking documents in this project.

In the classic vector space model proposed the term-specific weights in the document vectors are products of local and global parameters. The model is known as term frequency-inverse document frequency model. The weight vector for document d is :math:`bf{v}_d = [w_{1,d}, w_{2,d}, \ldots, w_{N,d}]^T`, where

.. math::

   w_{t,d} = \mathrm{tf}_{t,d} \cdot \log{\frac{|D|}{|\{d' \in D \, | \, t \in d'\}|}}

where

1. :math:`\mathrm{tf}_{t,d}`` is term frequency of term t in document :math:`d` (a local parameter)
2. :math:`\log{\frac{|D|}{|\{d' \in D \, | \, t \in d'\}|}}`` is inverse document frequency (a global parameter).
:math:`|D|` is the total number of documents in the document set; :math:`|\{d' \in D \, | \, t \in d'\}|`` is the number of documents containing the term :math:`t`.
Using the cosine the similarity between document dj and query q can be calculated as:

.. math::

   \mathrm{sim}(d_j,q) = \frac{\mathbf{d_j} \cdot \mathbf{q}}{\left\| \mathbf{d_j} \right\| \left \| \mathbf{q} \right\|} = \frac{\sum _{i=1}^N w_{i,j}w_{i,q}}{\sqrt{\sum _{i=1}^N w_{i,j}^2}\sqrt{\sum _{i=1}^N w_{i,q}^2}}
