# -*- coding: utf-8 -*-

"""Utilities for VarGenPath."""

import pybiomart


def file_reader(path: str) -> list:
	"""
	Read text file.
	:param path: text file containing the variants
	:return: list of variants
	"""
	file = open(path, "r")
	content = [line for line in file.readline()]
	return content


def get_associated_genes(variants_list: list):
	"""
	Get associated gene information from BioMart.
	:param variants_list: the list with variant ids.
	:return: dataframe with gene information.
	"""
	server = pybiomart.Server(host='http://www.ensembl.org')
	mart = server['ENSEMBL_MART_SNP']
	dataset = mart['hsapiens_snp']
	variant_gene_df = dataset.query(attributes=['refsnp_id', 'ensembl_gene_stable_id', 'associated_gene'],
					filters={'snp_filter': variants_list})
	return variant_gene_df


def snps_genes_network(variants_genes_dict):
	pass
