#!/bin/bash
FICHIERS=/Volumes/dev/cahiers_du_journalisme/liste-mots/tokens/*
for fichier in $FICHIERS
  do cmd/tree-tagger-french $fichier > $fichier.trt
done