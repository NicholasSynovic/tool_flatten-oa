from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Engine,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.sql import func


class DB:
    def __init__(self, engine: Engine) -> None:
        self.engine: Engine = engine

        self.metadata: MetaData = MetaData()

        self.tables: dict[str, str] = {
            "works": "works",
        }

        self.createTables()

    def createTables(self) -> None:
        _: Table = Table(
            self.tables["works"],
            self.metadata,
            Column("id", String, primary_key=True),
            Column("doi", String, nullable=False),
            Column("doi_registration_agency", String),
            Column("display_name", String),
            Column("title", String),
            Column("publication_year", Integer),
            Column("publication_date", Date),
            Column("language", String),
            Column("pmid", String),
            Column("mag", String),
            Column("type", String),
            Column("type_crossref", String),
            Column("countries_distinct_count", Integer),
            Column("institutions_distinct_count", Integer),
            Column("cited_by_count", Integer),
            Column("is_retracted", Boolean, default=False),
            Column("is_paratext", Boolean, default=False),
            Column("locations_count", Integer),
            Column("referenced_works_count", Integer),
            Column(
                "updated_date",
                Date,
                nullable=False,
                server_default=func.current_date(),
            ),
            Column(
                "created_date",
                Date,
                nullable=False,
                server_default=func.current_date(),
            ),
            Column("authors_count", Integer),
            Column("concepts_count", Integer),
            Column("topics_count", Integer),
            Column("has_fulltext", Boolean, default=False),
        )

        self.metadata.create_all(bind=self.engine, checkfirst=True)


def main() -> None:
    engine: Engine = create_engine(url="sqlite:///test.db")
    DB(engine=engine)


if __name__ == "__main__":
    main()
