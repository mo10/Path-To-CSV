function Form1Create(Sender){
    OpenDialog1.Filter = 'CSV files (*.csv)|*.CSV';
}
//Click add button
function btn_addClick(Sender){
    //Open file select dialog
    if(OpenDialog1.Execute()){
        for(var i=0;i<OpenDialog1.Files.Count;i++){
            //check file exist,then add to ListView1
            if(FileExists(OpenDialog1.Files(i))){
                var isExist=false;
                //Check if file already in ListView1
                for(var j=0;j<ListView1.Items.Count;j++)
                    if(ListView1.Items(j).Caption == OpenDialog1.Files(i))
                        isExist=true;
                //file not already in ListView1,add file to ListView1
                if(!isExist){
                    var item = TListItem.Create(ListView1.Items);
                    ListView1.Items.AddItem(item);
                    item.Caption = OpenDialog1.Files(i);
                }
            }
        }
    }
}
//Click del button
function btn_delClick(Sender){
    //remove selected items from ListView1
    for(var i=ListView1.Items.Count;i>0;i--){
        if(ListView1.Items(i-1).Selected)
            ListView1.Items.Delete(i-1);
   }
}
//Click generate button
function btn_genClick(Sender){
    //check ListView1
    if(ListView1.Items.Count==0){
        ShowMessage("Please add the CSV file first.");
        return;
    }
  /* Create a new PCB */
    // CreateNewDocumentFromDocumentKind('PCB');
    // var Board = PCBServer.GetCurrentPCBBoard;
    // if (Board == Null)
    // {
    //      ShowWarning("Create new PCB failed!");
    //      return;
    // }
    //var SpIter = Board.SpatialIterator_Create();
    //SpIter.AddFilter_ObjectSet(MkSet(eRegionObject));
    //var Prim = SpIter.FirstPCBObject();

    var  StrList=TStringList.Create();
    /* Create a Region object */
    var Region = PCBServer.PCBObjectFactory(eRegionObject, eNoDimension, eCreate_Default);
    StrList.LoadFromFile(ListView1.Items(0).Caption);
    CSVparser(StrList(1),0);
    //for(var i=0;i<StrList.Count;i++){
        //ShowMessage(StrList(i).length);
    //    CSVparser(StrList(i),0);
    //}
}
function CSVparser(line,pos) {
    var first_pos = line.indexOf(',');
    var second_pos = line.indexOf(',',first_pos+1);
    var third_pos = line.indexOf(',',second_pos+1);
    var end_pos = line.length;
    ShowMessage(line.substring(0,first_pos));
    ShowMessage(line.substring(first_pos+1,second_pos));
    ShowMessage(line.substring(second_pos+1,third_pos));
    ShowMessage(line.substring(third_pos+1,end_pos));
}
function trim(line,char) {

}
// Altium Designer Script Editor is like shit.

