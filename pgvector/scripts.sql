create database document_search;

create extension if not exists vector;

create table if not exists documents
(
  id        bigserial primary key,
  content   text,
  file_name text,
  embedding vector(1536)
);

create or replace function match_documents(
  query_embedding vector(1536),
  similarity_threshold float,
  match_count int
)
  returns table
  (
    id         bigint,
    content    text,
    file_name  text,
    similarity float
  )
  language plpgsql
as
$$
begin
  return query
    select d.id,
           d.content,
           d.file_name,
           1 - (d.embedding <=> query_embedding) as similarity
    from documents d
    where 1 - (d.embedding <=> query_embedding) > similarity_threshold
    order by d.embedding <=> query_embedding
    limit match_count;
end;
$$;
