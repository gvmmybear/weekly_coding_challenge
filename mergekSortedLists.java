class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode myNode = new ListNode();
        ListNode head = myNode;
        int minNodeIndex = 0;
        int nodeNullCount = 0;
        int minNodeValue = 0;
        boolean hasMinVal = false;
       
        while(nodeNullCount < lists.length){
            nodeNullCount = 0;
            for(int i = 0; i < lists.length; i++){
                if(lists[i] != null){
                    if(!hasMinVal){
                        hasMinVal = true;
                        minNodeValue = lists[i].val;
                        minNodeIndex = i;
                    }else if(lists[i].val < minNodeValue){
                        minNodeValue = lists[i].val;
                        minNodeIndex = i;
                    }
                }else{
                    nodeNullCount += 1;
                }
            }
            if(nodeNullCount != lists.length){
                myNode.val = minNodeValue;
                myNode.next = nodeNullCount < lists.length - 1? new ListNode() : null;
                myNode = myNode.next;
                lists[minNodeIndex] = lists[minNodeIndex].next;
                hasMinVal = false;
                
            }
        }
        ListNode node = new ListNode();
        return head;
    }
}
