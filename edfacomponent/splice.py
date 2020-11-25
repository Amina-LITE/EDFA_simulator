from edfacomponent.component import component
#from dbconnection import run_query
import time
class splice(component):
    def __init__(self, splice_loss, cname, ctype, clayer, cfamily='splice'):
        #query_str = "select lossarray from cktpack.tbl_splice where component_family='Splice' and component_type='" + ctype + "';"
        #start_time = time.time()
        #result = run_query(query_str, True)
        #print("--- %s seconds ---" % (time.time() - start_time)) 
        
        self.splice_loss = splice_loss
        super().__init__(cname, ctype, cfamily , clayer)

    def getSpliceLoss(self):
        return self.splice_loss
    
    def setSpliceLoss(self, splice_loss):
        self.splice_loss = splice_loss
