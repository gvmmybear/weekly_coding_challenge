class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode myNode = new ListNode();
        int minNodeIndex = 0;
        int nodeNullCount = 0;
        int minNodeValue;
       
        while(nodeNullCount < lists.length){
            for(int i = 0; i < lists.length; i++){
                if(lists[i] != null){
                    lists[i] = lists[i].next;
                }else{
                    continue;
                }
            }
            nodeNullCount += 1;
        }
    
        ListNode node = new ListNode();
        return node;
    }
}
