# Back End Assignment - REUNION
## Problem Statement
- Build APIs for a social media platform in either NodeJS or Python
- The API should support features like getting a user profile, follow a user, upload a post, delete a post, like a post, unlike a liked post, and comment on a post
- Design the database schema and implement in PostgreSQL or MongoDB

## API Endpoints
- <u>GET</u>: /api/user should authenticate the request and return the respective user profile.<br>
    `RETURN: User Name, number of followers & followings.`
- <u>GET</u>: api/posts/{id} would return a single post with {id} populated with its number of likes and comments
- <u>GET</u>: /api/all_posts would return all posts created by authenticated user sorted by post time.<br>
    `RETURN: For each post return the following values`
    <ol>
    <li>id: ID of the post</li>
    <li>title: Title of the post</li>
    <li>desc: Description of the post</li>
    <li>created_at: Date and time when the post was created</li>
    <li>comments: Array of comments, for the particular post</li>
    <li>likes: Number of likes for the particular post</li>
    </ol>
- <u>POST</u>: /api/follow/{id} authenticated user would follow user with {id}
- <u>POST</u>: /api/unfollow/{id} authenticated user would unfollow a user with {id}
- <u>POST</u>: api/posts/ would add a new post created by the authenticated user.<br>
    `RETURN: Post-ID, Title, Description, Created Time(UTC).`
    - Input: Title, Description
- <u>POST</u>: /api/like/{id} would like the post with {id} by the authenticated user.
- <u>POST</u>: /api/unlike/{id} would unlike the post with {id} by the authenticated user.
- <u>POST</u>: /api/comment/{id} add comment for post with {id} by the authenticated user.
- <u>POST</u>: /api/authenticate should perform user authentication and return a JWT token.<br>
    `RETURN: JWT token`
    - INPUT: Email, Password
    > NOTE: Use dummy email & password for authentication. No need to create endpoint for registering new user.`
- <u>DELETE</u>: api/posts/{id} would delete post with {id} created by the authenticated user.<br>
    `Return: Comment-ID`
    Input: Comment

### Stacks

- Backend: NodeJS (using ExpressJS or Koa) or Python (using Django). Use other helping libraries.
- Database: PostgreSQL or MongoDB

# Instructions

- Implement the mentioned functionalities by writing your code & hosting it on [Render](https://render.com/).
- Submit the Render hosted link for the deployed APIs and Github or Gitlab public repository link for the deployed code in the form below.
- Provide the list of the functional testcases specific to each API endpoint with description in an Excel sheet ([sample sheet](https://www.notion.so/Back-End-Assignment-REUNION-bd5e48b7aab54e91b6ee8829c3e30c4a)) & submit it via the form below.<br>
    > 💬 Sample excel file for tests
    [Sample Test Case](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04d601bc-47d5-45f9-bcd5-eba09e7b6acc/Untitled.xlsx)
    - Don’t write all the testcase but try to focus on the important testcases according to your understanding.
    
- Implement the testcases using the language specific framework or library like Mocha or Chai.js for Node.
    - Commit the testcase code in the git repo & provide the commands to run the testcases.
- Create a single docker file for running the full web app under a single docker image. Commit the docker file under the same repo & provide the link.
    - Please note docker file should take care of the database, running testcases & other dependencies installation.