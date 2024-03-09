from SigProfilerExtractor import sigpro as sig
def main_function():
 sig.sigProfilerExtractor("vcf", "renal2023_output","/Users/sunyuqi/Desktop/病理科/肾癌2023的副本",reference_genome="GRCh37",opportunity_genome = "GRCh37", context_type = "default", exome = False,minimum_signatures=1,maximum_signatures=4)
if __name__=="__main__":
    main_function()