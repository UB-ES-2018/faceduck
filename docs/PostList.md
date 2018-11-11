# Situations in which we want a PostList

1. User profiles
2. Search results, query
3. Search results, tag
4. Personal feed

# APIs that satisfy each situation

## User profiles (implemented)

Search posts by user. Satisfied by:

```
POST /post/search
```

With the parameter ```author-id```.

## Search results, query 

Search posts by text content. Satisfied by:

```
POST /post/search
```

With the parameter ```query```.

## Search results, tag

Search posts by tag. Satisfied by:

```
POST /post/search
```

With the parameter ```tag```.

## Personal feed 

Unimplemented.