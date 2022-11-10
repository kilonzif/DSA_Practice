class Node {
  constructor(element) {
    this.element = element;
    this.next = null;
  }
}
//linkedlist class
class LinkedList {
  constructor() {
    this.head = null;
  }
  addNode(element) {
    var node = new Node(element);
    node.next = this.head;
    this.head = node;
    return this;
  }
}
function reverseNode(list) {
  let prev = null;
  let next = null;
  let current = list;
  while (current != null) {
    next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
}
