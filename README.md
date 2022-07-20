# Action2Graph

## About

A simple test of leveraging GitHub actions to perform transforms on data graph or other sources.  
Have seen several groups doing some interesting transforms on graphs or other data structures
into graphs.  Was curious what a repo using GitHub Actions looked like that could take input 
commits and then generate out the results.

This could, for example, be done on a CSV of sources that generates out a graph representation.  Or JSON-LD to other RDF serializations.


## SHACL

The basic plumbing is in place.  The [shacl-job.yml](./.github/workflows/schacl-job.yml) runs the [orgfiles.py](scripts/orgfiles.py).  We need to pass the arguements better, or filter the correct 
files for processing.  Also, we could leverage the reportlab style
report generation for PDFs.  

## References

[GitHub actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
