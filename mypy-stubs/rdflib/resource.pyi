from typing import Any, Iterable, Iterator, Tuple

from _typeshed import Incomplete
from rdflib.graph import Graph, Seq
from rdflib.term import Node

class Resource:
    def __init__(self, graph: Graph, subject: Node) -> None: ...
    graph: Incomplete
    identifier: Incomplete
    def add(self, p: Node, o: Node) -> None: ...
    def remove(self, p: Node, o: Node | None = ...) -> None: ...
    def set(self, p: Node, o: Node) -> None: ...
    def subjects(self, predicate: Any | None = ...) -> Iterable[Node]: ...
    def predicates(self, o: Incomplete | None = ...) -> Iterable[Node]: ...
    def objects(self, predicate: Any | None = ...) -> Iterable[Node]: ...
    def subject_predicates(self) -> Iterator[Tuple[Node, Node]]: ...
    def subject_objects(self) -> Iterator[Tuple[Node, Node]]: ...
    def predicate_objects(self) -> Iterator[Tuple[Node, Node]]: ...
    def value(
        self, p: Node, o: Node | None = ..., default: Any | None = ..., any: bool = ...
    ) -> Any: ...
    def label(self) -> Any: ...
    def comment(self) -> Any: ...
    def items(self) -> Iterator[Any]: ...
    def transitive_objects(
        self, predicate: Node, remember: Any | None = ...
    ) -> Iterator[Any]: ...
    def transitive_subjects(
        self, predicate: Node, remember: Any | None = ...
    ) -> Iterator[Any]: ...
    def seq(self) -> Seq | None: ...
    def qname(self) -> Any: ...